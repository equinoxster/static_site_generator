import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_parentnode_basic_html(self):
        node = ParentNode("div", [LeafNode("span", "Hello")])
        self.assertEqual(node.to_html(), "<div><span>Hello</span></div>")

    def test_parentnode_with_props(self):
        node = ParentNode("div", [LeafNode("span", "Hello")], props={"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><span>Hello</span></div>')

    def test_parentnode_nested(self):
        child = ParentNode("ul", [LeafNode("li", "Item 1"), LeafNode("li", "Item 2")])
        node = ParentNode("div", [child])
        self.assertEqual(node.to_html(), "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>")

    def test_parentnode_multiple_children(self):
        node = ParentNode("div", [LeafNode("span", "A"), LeafNode("span", "B")])
        self.assertEqual(node.to_html(), "<div><span>A</span><span>B</span></div>")

    def test_parentnode_empty_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("", [LeafNode("span", "A")])

    def test_parentnode_none_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "A")])

    def test_parentnode_none_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_parentnode_repr(self):
        node = ParentNode("div", [LeafNode("span", "A")], props={"id": "main"})
        self.assertIn("ParentNode", repr(node))
        self.assertIn("div", repr(node))

    def test_parentnode_deeply_nested(self):
        # 4 levels deep: div > section > article > span
        node = ParentNode(
            "div", [
                ParentNode(
                    "section", [
                        ParentNode(
                            "article", [
                                LeafNode("span", "Deep Value")
                            ]
                        )
                    ]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><article><span>Deep Value</span></article></section></div>"
        )

    def test_parentnode_deeply_nested_with_siblings(self):
        # 4 levels deep with siblings at each level
        node = ParentNode(
            "div", [
                LeafNode("h1", "Title"),
                ParentNode(
                    "section", [
                        LeafNode("p", "Intro"),
                        ParentNode(
                            "article", [
                                LeafNode("span", "Deep Value"),
                                LeafNode("span", "Another Value")
                            ]
                        )
                    ]
                ),
                LeafNode("footer", "End")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><h1>Title</h1><section><p>Intro</p><article><span>Deep Value</span><span>Another Value</span></article></section><footer>End</footer></div>"
        )

    def test_parentnode_deeply_nested_with_props(self):
        # 4 levels deep: div (with props) > section (with props) > article (with props) > span (with props)
        node = ParentNode(
            "div", [
                ParentNode(
                    "section", [
                        ParentNode(
                            "article", [
                                LeafNode("span", "Deep Value", props={"style": "color:red"})
                            ], props={"data-article": "yes"})
                    ], props={"class": "section-class"})
            ], props={"id": "main-div"})
        self.assertEqual(
            node.to_html(),
            '<div id="main-div"><section class="section-class"><article data-article="yes"><span style="color:red">Deep Value</span></article></section></div>'
        )

    def test_parentnode_deeply_nested_with_sibling_props(self):
        # 4 levels deep with siblings and props at various levels
        node = ParentNode(
            "div", [
                LeafNode("h1", "Title", props={"class": "header"}),
                ParentNode(
                    "section", [
                        LeafNode("p", "Intro", props={"id": "intro-p"}),
                        ParentNode(
                            "article", [
                                LeafNode("span", "Deep Value", props={"data-x": "1"}),
                                LeafNode("span", "Another Value")
                            ], props={"class": "art"})
                    ], props={"data-section": "main"})
                ,
                LeafNode("footer", "End", props={"role": "contentinfo"})
            ], props={"id": "main-div"})
        self.assertEqual(
            node.to_html(),
            '<div id="main-div"><h1 class="header">Title</h1><section data-section="main"><p id="intro-p">Intro</p><article class="art"><span data-x="1">Deep Value</span><span>Another Value</span></article></section><footer role="contentinfo">End</footer></div>'
        )

if __name__ == "__main__":
    unittest.main()
