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

    
class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_image_at_start(self):
        # Test an image at the start of text
        node = TextNode(
            "![start image](https://example.com/start.jpg) followed by text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("start image", TextType.IMAGE, "https://example.com/start.jpg"),
                TextNode(" followed by text", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_image_at_end(self):
        # Test an image at the end of text
        node = TextNode(
            "Text followed by ![end image](https://example.com/end.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text followed by ", TextType.TEXT),
                TextNode("end image", TextType.IMAGE, "https://example.com/end.jpg"),
            ],
            new_nodes,
        )
    
    def test_only_image(self):
        # Test a node containing only an image
        node = TextNode(
            "![solo image](https://example.com/solo.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("solo image", TextType.IMAGE, "https://example.com/solo.jpg"),
            ],
            new_nodes,
        )
    
    def test_multiple_adjacent_images(self):
        # Test text with adjacent images
        node = TextNode(
            "![first](https://example.com/1.jpg)![second](https://example.com/2.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://example.com/1.jpg"),
                TextNode("second", TextType.IMAGE, "https://example.com/2.jpg"),
            ],
            new_nodes,
        )
    
    def test_non_text_node(self):
        # Test that non-TEXT nodes are left unchanged
        node = TextNode("bold text with ![image](https://example.com/img.jpg)", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [node],  # Should be unchanged since it's not a TextType.TEXT
            new_nodes,
        )
    
    def test_empty_nodes_list(self):
        # Test with an empty list of nodes
        new_nodes = split_nodes_image([])
        self.assertListEqual([], new_nodes)
    
    def test_no_images_in_text(self):
        # Test text without any images
        node = TextNode("This is plain text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_node_with_url(self):
        # Test that URL is preserved in text nodes when images are extracted
        node = TextNode(
            "Link text ![image](https://example.com/img.jpg) more text",
            TextType.TEXT,
            "https://example.com/link"
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Link text ", TextType.TEXT, "https://example.com/link"),
                TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
                TextNode(" more text", TextType.TEXT, "https://example.com/link"),
            ],
            new_nodes,
        )
    
    def test_complex_mixed_content(self):
        # Test with a mix of nodes, some with images, some without
        node1 = TextNode("Text with ![img](https://example.com/1.jpg)", TextType.TEXT)
        node2 = TextNode("No images here", TextType.TEXT)
        node3 = TextNode("Bold text", TextType.BOLD)
        node4 = TextNode("![another](https://example.com/2.jpg) More text", TextType.TEXT)
        
        new_nodes = split_nodes_image([node1, node2, node3, node4])
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "https://example.com/1.jpg"),
                TextNode("No images here", TextType.TEXT),
                TextNode("Bold text", TextType.BOLD),
                TextNode("another", TextType.IMAGE, "https://example.com/2.jpg"),
                TextNode(" More text", TextType.TEXT),
            ],
            new_nodes,
        )
    

if __name__ == "__main__":
    unittest.main()
