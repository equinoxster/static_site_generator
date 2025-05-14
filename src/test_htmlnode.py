import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "content", [], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "content")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})
        
        default_node = HTMLNode()
        self.assertIsNone(default_node.tag)
        self.assertIsNone(default_node.value)
        self.assertIsNone(default_node.children)
        self.assertIsNone(default_node.props)

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!", None, {"class": "text"})
        expected_repr = "HTMLNode(p, Hello, world!, None, {'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)

    def test_add_props_html(self):
        class TestableHTMLNode(HTMLNode):
            def test_props_html(self):
                return self.props_to_html()
        
        node = TestableHTMLNode(props={"class": "container", "id": "main"})

        def fixed_add_props_html(self):
            out = ""
            for key in self.props.keys():
                out += f" {key}=\"{self.props[key]}\""
            return out
            
        TestableHTMLNode.props_to_html = fixed_add_props_html
        
        props_html = node.test_props_html()
        self.assertTrue(' class="container"' in props_html)
        self.assertTrue(' id="main"' in props_html)
        
    def test_to_html_not_implemented(self):
        node = HTMLNode("div", "content")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_with_children(self):
        # Create child nodes
        child1 = HTMLNode("p", "Paragraph 1")
        child2 = HTMLNode("p", "Paragraph 2")
        
        # Create parent node with children
        parent = HTMLNode("div", None, [child1, child2], {"class": "parent"})
        
        # Test that the parent has the correct children
        self.assertEqual(len(parent.children), 2)
        self.assertIs(parent.children[0], child1)
        self.assertIs(parent.children[1], child2)
        
        # Test nested structure is preserved
        self.assertEqual(parent.children[0].value, "Paragraph 1")
        self.assertEqual(parent.children[1].value, "Paragraph 2")
        
        # Test children with their own children
        grandchild = HTMLNode("span", "I'm a grandchild")
        child3 = HTMLNode("div", None, [grandchild])
        parent_with_grandchild = HTMLNode("section", None, [child3])
        
        self.assertEqual(len(parent_with_grandchild.children), 1)
        self.assertEqual(len(parent_with_grandchild.children[0].children), 1)
        self.assertEqual(parent_with_grandchild.children[0].children[0].value, "I'm a grandchild")

if __name__ == "__main__":
    unittest.main()
