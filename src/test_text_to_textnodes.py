import unittest
from text_to_textnodes import *

class TestTextToTextNode(unittest.TestCase):
    def test_example(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        actual = text_to_textnode(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(expected, actual)
        
    def test_plain_text(self):
        """Test with plain text only, no Markdown formatting."""
        text = "This is just plain text with no formatting."
        actual = text_to_textnode(text)
        expected = [TextNode("This is just plain text with no formatting.", TextType.TEXT)]
        self.assertEqual(expected, actual)
        
    def test_bold_only(self):
        """Test with only bold formatting."""
        text = "**Bold text**"
        actual = text_to_textnode(text)
        expected = [TextNode("Bold text", TextType.BOLD)]
        self.assertEqual(expected, actual)
        
    def test_italic_only(self):
        """Test with only italic formatting."""
        text = "_Italic text_"
        actual = text_to_textnode(text)
        expected = [TextNode("Italic text", TextType.ITALIC)]
        self.assertEqual(expected, actual)
        
    def test_code_only(self):
        """Test with only code formatting."""
        text = "`Code text`"
        actual = text_to_textnode(text)
        expected = [TextNode("Code text", TextType.CODE)]
        self.assertEqual(expected, actual)
        
    def test_link_only(self):
        """Test with only a link."""
        text = "[Link text](https://example.com)"
        actual = text_to_textnode(text)
        expected = [TextNode("Link text", TextType.LINK, "https://example.com")]
        self.assertEqual(expected, actual)
        
    def test_image_only(self):
        """Test with only an image."""
        text = "![Image alt](https://example.com/image.jpg)"
        actual = text_to_textnode(text)
        expected = [TextNode("Image alt", TextType.IMAGE, "https://example.com/image.jpg")]
        self.assertEqual(expected, actual)
        
    def test_multiple_bold(self):
        """Test with multiple bold sections."""
        text = "This has **multiple** bold **sections**."
        actual = text_to_textnode(text)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("multiple", TextType.BOLD),
            TextNode(" bold ", TextType.TEXT),
            TextNode("sections", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)
        
    def test_multiple_italic(self):
        """Test with multiple italic sections."""
        text = "This has _multiple_ italic _sections_."
        actual = text_to_textnode(text)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("multiple", TextType.ITALIC),
            TextNode(" italic ", TextType.TEXT),
            TextNode("sections", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)
        
    def test_multiple_code(self):
        """Test with multiple code sections."""
        text = "This has `multiple` code `sections`."
        actual = text_to_textnode(text)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("multiple", TextType.CODE),
            TextNode(" code ", TextType.TEXT),
            TextNode("sections", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)
        
    def test_multiple_links(self):
        """Test with multiple links."""
        text = "This has [link one](https://example.com) and [link two](https://example.org)."
        actual = text_to_textnode(text)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("link one", TextType.LINK, "https://example.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link two", TextType.LINK, "https://example.org"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)
        
    def test_multiple_images(self):
        """Test with multiple images."""
        text = "This has ![image one](https://example.com/1.jpg) and ![image two](https://example.com/2.jpg)."
        actual = text_to_textnode(text)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("image one", TextType.IMAGE, "https://example.com/1.jpg"),
            TextNode(" and ", TextType.TEXT),
            TextNode("image two", TextType.IMAGE, "https://example.com/2.jpg"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)
        
        
    def test_complex_formatting(self):
        """Test with complex mixed formatting."""
        text = "**Bold** then `code` with _italic_ and ![img](https://example.com/img.jpg) plus [link](https://example.com)."
        actual = text_to_textnode(text)
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" then ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://example.com/img.jpg"),
            TextNode(" plus ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)
        
