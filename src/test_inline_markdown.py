import unittest

from textnode import *
from inline_markdown import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_normal_text_with_code_delimiter(self):
        # Test splitting text with ` delimiter for code text
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),  
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_split_normal_text_with_bold_delimiter(self):
        # Test splitting text with ** delimiter for bold text
        node = TextNode("This is **bold text** in a sentence", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),  
            TextNode("bold text", TextType.BOLD),
            TextNode(" in a sentence", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_split_normal_text_with_italic_delimiter(self):
        # Test splitting text with _ delimiter for italic text
        node = TextNode("This is _italic text_ in a sentence", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),  
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in a sentence", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_text_starting_with_delimiter(self):
        # Test text that starts with a delimiter
        node = TextNode("`code block` at the beginning", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("code block", TextType.CODE),
            TextNode(" at the beginning", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_text_ending_with_delimiter(self):
        # Test text that ends with a delimiter
        node = TextNode("at the end **bold text**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("at the end ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
        ]
        self.assertEqual(result, expected)
    
    def test_multiple_delimiters(self):
        # Test text with multiple instances of the same delimiter
        node = TextNode("This has **bold** and more **bold text**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and more ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
        ]
        self.assertEqual(result, expected)
    
    def test_multiple_nodes(self):
        # Test multiple nodes in the input list
        node1 = TextNode("Text with `code`", TextType.TEXT)
        node2 = TextNode("More text with `another code`", TextType.TEXT)
        node3 = TextNode("This is a bold header", TextType.BOLD)  # Should be left unchanged
        result = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("More text with ", TextType.TEXT),
            TextNode("another code", TextType.CODE),
            TextNode("This is a bold header", TextType.BOLD),  # Unchanged
        ]
        self.assertEqual(result, expected)
    
    def test_adjacent_delimiters(self):
        # Test text with adjacent delimiters of different types (require multiple passes)
        node = TextNode("This is **bold text**_italic text_", TextType.TEXT)
        # First split by ** for bold
        intermediate = split_nodes_delimiter([node], "**", TextType.BOLD)
        # Then split the results by _ for italic
        result = split_nodes_delimiter(intermediate, "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode("italic text", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
