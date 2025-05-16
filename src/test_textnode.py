import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "")
        node2 = TextNode("This is a text node", TextType.BOLD, "")

        self.assertEqual(node, node2)

        node.url = "www.google.com"
        node2.url = "www.google.com"

        self.assertEqual(node, node2)

    def test_notEq(self):
        node = TextNode("This is", TextType.ITALIC, "www.atlassian.com")
        node2 = TextNode("Not equal", TextType.ITALIC, "www.atlassian.com")

        self.assertNotEqual(node, node2)

        node.text = "Same text"
        node.text_type = TextType.TEXT
        node2.text = "Same text"

        self.assertNotEqual(node, node2)

        node.text_type = TextType.ITALIC
        node2.url = "www.google.com"

    def test_repr(self):
        node = TextNode("Text", TextType.BOLD, "www.google.com")

        self.assertEqual("TextNode(Text, TextType.BOLD, www.google.com)", node.__repr__())

    def test_text_type_text(self):
        tn = TextNode("Hello", TextType.TEXT, None)
        node = text_node_to_html_node(tn)
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Hello")

    def test_text_type_bold(self):
        tn = TextNode("Bold", TextType.BOLD, None)
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, "Bold")

    def test_text_type_italic(self):
        tn = TextNode("Italic", TextType.ITALIC, None)
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "i")
        self.assertEqual(node.value, "Italic")

    def test_text_type_code(self):
        tn = TextNode("print('hi')", TextType.CODE, None)
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "code")
        self.assertEqual(node.value, "print('hi')")

    def test_text_type_link(self):
        tn = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Boot.dev")

    def test_text_type_image(self):
        tn = TextNode("Alt text", TextType.IMAGE, "img.png")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src": "img.png", "alt": "Alt text"})

    def test_invalid_text_type_raises(self):
        class FakeType: pass
        tn = TextNode("oops", FakeType, None)
        with self.assertRaises(Exception):
            text_node_to_html_node(tn)



if __name__ == "__main¨":
    unittest.main()
