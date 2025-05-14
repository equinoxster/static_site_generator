import unittest

from textnode import TextNode, TextType

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
        node.text_type = TextType.NORMAL
        node2.text = "Same text"

        self.assertNotEqual(node, node2)

        node.text_type = TextType.ITALIC
        node2.url = "www.google.com"

    def test_repr(self):
        node = TextNode("Text", TextType.BOLD, "www.google.com")

        self.assertEqual("TextNode(Text, TextType.BOLD, www.google.com)", node.__repr__())



if __name__ == "__main¨":
    unittest.main()
