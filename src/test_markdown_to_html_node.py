import unittest
from markdown_to_html_node import *


class TestMarkdownToHtmlNode(unittest.TestCase):
    
    # PARAGRAPH TESTS
    def test_single_paragraph(self):
        """Test a simple single paragraph"""
        md = "This is a simple paragraph."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is a simple paragraph.</p></div>")
    
    def test_multiple_paragraphs(self):
        """Test multiple paragraphs with inline formatting"""
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_paragraph_with_all_inline_formatting(self):
        """Test paragraph with bold, italic, code, links, and images"""
        md = "This has **bold**, _italic_, `code`, ![image](url.png), and [link](url.com) text."
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Just verify it contains the expected elements without exact match due to potential ordering issues
        self.assertIn('<b>bold</b>', html)
        self.assertIn('<i>italic</i>', html)
        self.assertIn('<code>code</code>', html)
        self.assertIn('<img src="url.png" alt="image">', html)
        self.assertIn('<a href="url.com">link</a>', html)
    
    def test_paragraph_whitespace_normalization(self):
        """Test that paragraph whitespace is properly normalized"""
        md = """This    has     lots
        of       whitespace
        and   newlines"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><p>This has lots of whitespace and newlines</p></div>'
        self.assertEqual(html, expected)

    # CODE BLOCK TESTS
    def test_simple_codeblock(self):
        """Test a simple code block"""
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_codeblock_with_indentation(self):
        """Test code block with consistent indentation"""
        md = """
```
    def hello():
        print("Hello")
        return True
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><pre><code>def hello():\n    print("Hello")\n    return True\n</code></pre></div>'
        self.assertEqual(html, expected)
    
    def test_codeblock_empty(self):
        """Test empty code block"""
        md = "```\n```"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><pre><code>\n</code></pre></div>'
        self.assertEqual(html, expected)
    
    def test_codeblock_single_line(self):
        """Test single line code block"""
        md = """
```
print("hello")
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><pre><code>print("hello")\n</code></pre></div>'
        self.assertEqual(html, expected)

    # HEADING TESTS
    def test_heading_h1(self):
        """Test H1 heading"""
        md = "# This is an H1"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><h1>This is an H1</h1></div>'
        self.assertEqual(html, expected)
    
    def test_heading_h2(self):
        """Test H2 heading"""
        md = "## This is an H2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><h2>This is an H2</h2></div>'
        self.assertEqual(html, expected)
    
    def test_heading_h6(self):
        """Test H6 heading (maximum level)"""
        md = "###### This is an H6"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><h6>This is an H6</h6></div>'
        self.assertEqual(html, expected)
    
    def test_heading_with_inline_formatting(self):
        """Test heading with inline formatting"""
        md = "## This has **bold** and _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><h2>This has <b>bold</b> and <i>italic</i> text</h2></div>'
        self.assertEqual(html, expected)
    
    def test_multiple_headings(self):
        """Test multiple headings of different levels"""
        md = """# Main Title

## Subtitle

### Section

Text paragraph here."""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><h1>Main Title</h1><h2>Subtitle</h2><h3>Section</h3><p>Text paragraph here.</p></div>'
        self.assertEqual(html, expected)

    # QUOTE TESTS
    def test_single_line_quote(self):
        """Test single line blockquote"""
        md = "> This is a quote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><blockquote>This is a quote</blockquote></div>'
        self.assertEqual(html, expected)
    
    def test_multi_line_quote(self):
        """Test multi-line blockquote"""
        md = """> This is a quote
> that spans multiple
> lines"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><blockquote>This is a quote that spans multiple lines</blockquote></div>'
        self.assertEqual(html, expected)
    
    def test_quote_with_inline_formatting(self):
        """Test blockquote with inline formatting"""
        md = "> This quote has **bold** and _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><blockquote>This quote has <b>bold</b> and <i>italic</i> text</blockquote></div>'
        self.assertEqual(html, expected)

    # UNORDERED LIST TESTS
    def test_single_item_unordered_list(self):
        """Test unordered list with single item"""
        md = "- Single item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ul><li>Single item</li></ul></div>'
        self.assertEqual(html, expected)
    
    def test_multi_item_unordered_list(self):
        """Test unordered list with multiple items"""
        md = """- First item
- Second item
- Third item"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>'
        self.assertEqual(html, expected)
    
    def test_unordered_list_with_inline_formatting(self):
        """Test unordered list with inline formatting"""
        md = """- Item with **bold** text
- Item with _italic_ text
- Item with `code` text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ul><li>Item with <b>bold</b> text</li><li>Item with <i>italic</i> text</li><li>Item with <code>code</code> text</li></ul></div>'
        self.assertEqual(html, expected)

    # ORDERED LIST TESTS
    def test_single_item_ordered_list(self):
        """Test ordered list with single item"""
        md = "1. Single item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ol><li>Single item</li></ol></div>'
        self.assertEqual(html, expected)
    
    def test_multi_item_ordered_list(self):
        """Test ordered list with multiple items"""
        md = """1. First item
2. Second item
3. Third item"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>'
        self.assertEqual(html, expected)
    
    def test_ordered_list_with_inline_formatting(self):
        """Test ordered list with inline formatting"""
        md = """1. Item with **bold** text
2. Item with _italic_ text
3. Item with `code` text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ol><li>Item with <b>bold</b> text</li><li>Item with <i>italic</i> text</li><li>Item with <code>code</code> text</li></ol></div>'
        self.assertEqual(html, expected)
    
    def test_ordered_list_non_sequential_numbers(self):
        """Test ordered list with non-sequential numbers"""
        md = """1. First item
5. Second item
10. Third item"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>'
        self.assertEqual(html, expected)

    # MIXED CONTENT TESTS
    def test_all_block_types_together(self):
        """Test document with all block types"""
        md = """# Main Heading

This is a paragraph with **bold** text.

## Subheading

> This is a blockquote with _italic_ text.

- Item one
- Item two

1. First
2. Second

```
def code_example():
    return "Hello World"
```

Final paragraph."""
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        
        # Verify the structure contains all expected elements
        self.assertIn('<h1>Main Heading</h1>', html)
        self.assertIn('<p>This is a paragraph with <b>bold</b> text.</p>', html)
        self.assertIn('<h2>Subheading</h2>', html)
        self.assertIn('<blockquote>This is a blockquote with <i>italic</i> text.</blockquote>', html)
        self.assertIn('<ul><li>Item one</li><li>Item two</li></ul>', html)
        self.assertIn('<ol><li>First</li><li>Second</li></ol>', html)
        self.assertIn('<pre><code>def code_example():\n    return "Hello World"\n</code></pre>', html)
        self.assertIn('<p>Final paragraph.</p>', html)
        self.assertTrue(html.startswith('<div>'))
        self.assertTrue(html.endswith('</div>'))

    # EDGE CASES
    def test_empty_markdown(self):
        """Test empty markdown input"""
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div></div>'
        self.assertEqual(html, expected)
    
    def test_whitespace_only_markdown(self):
        """Test markdown with only whitespace"""
        md = "   \n\n   \n  "
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div></div>'
        self.assertEqual(html, expected)
    
    def test_single_newline_paragraph(self):
        """Test paragraph separated by single newlines (should be one paragraph)"""
        md = """First line
Second line
Third line"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><p>First line Second line Third line</p></div>'
        self.assertEqual(html, expected)
    
    def test_complex_inline_formatting(self):
        """Test complex inline formatting combinations"""
        md = "Text with **bold text** and `code text` and more."
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Should handle formatting appropriately
        self.assertIn('<b>bold text</b>', html)
        self.assertIn('<code>code text</code>', html)
    
    def test_heading_without_space(self):
        """Test heading without space after #"""
        md = "#Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><h1>Heading</h1></div>'
        self.assertEqual(html, expected)
    
    def test_list_with_extra_spaces(self):
        """Test lists with extra spaces"""
        md = """- Item with    extra   spaces
- Another item
- Item without space"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # List items preserve their original spacing in this implementation
        self.assertIn('<li>Item with    extra   spaces</li>', html)
        self.assertIn('<li>Another item</li>', html)
        self.assertIn('<li>Item without space</li>', html)

    # RETURN TYPE TESTS
    def test_return_type_is_parent_node(self):
        """Test that function returns a ParentNode"""
        md = "# Test"
        node = markdown_to_html_node(md)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, "div")
        self.assertIsNotNone(node.children)
    
    def test_children_are_proper_html_nodes(self):
        """Test that children are proper HTML nodes"""
        md = """# Heading

Paragraph text

```
code
```"""
        node = markdown_to_html_node(md)
        
        # Should have 3 children
        self.assertEqual(len(node.children), 3)
        
        # First child should be h1
        h1_node = node.children[0]
        self.assertIsInstance(h1_node, ParentNode)
        self.assertEqual(h1_node.tag, "h1")
        
        # Second child should be p
        p_node = node.children[1]
        self.assertIsInstance(p_node, ParentNode)
        self.assertEqual(p_node.tag, "p")
        
        # Third child should be pre
        pre_node = node.children[2]
        self.assertIsInstance(pre_node, ParentNode)
        self.assertEqual(pre_node.tag, "pre")