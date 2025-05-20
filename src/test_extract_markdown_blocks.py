import unittest
from extract_markdown_blocks import markdown_to_blocks

class Test_Markdown_to_Blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_input(self):
        """Test that an empty string results in an empty list of blocks"""
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
        
    def test_whitespace_only_input(self):
        """Test that a string with only whitespace results in an empty list of blocks"""
        md = "   \n\n   \n   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
        
    def test_headers(self):
        """Test that headers are correctly identified as separate blocks"""
        md = """# Heading 1

## Heading 2
This is part of heading 2 block

### Heading 3"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "## Heading 2\nThis is part of heading 2 block",
                "### Heading 3"
            ],
        )
        
    def test_code_blocks(self):
        """Test that code blocks are correctly identified"""
        md = """Here is a code block:

```python
def hello_world():
    print("Hello, World!")
```

And here is some text after."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Here is a code block:",
                "```python\ndef hello_world():\n    print(\"Hello, World!\")\n```",
                "And here is some text after."
            ],
        )
        
    def test_blockquotes(self):
        """Test that blockquotes are correctly identified"""
        md = """Here's a quote:

> This is a blockquote
> It continues on this line

Normal text continues here."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Here's a quote:",
                "> This is a blockquote\n> It continues on this line",
                "Normal text continues here."
            ],
        )
        
    def test_multiple_empty_lines(self):
        """Test that multiple empty lines between blocks are handled correctly"""
        md = """First paragraph.



Second paragraph."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph.",
                "Second paragraph."
            ],
        )
        
    def test_ordered_lists(self):
        """Test that ordered lists are correctly identified"""
        md = """Here's an ordered list:

1. First item
2. Second item
3. Third item

And some text after."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Here's an ordered list:",
                "1. First item\n2. Second item\n3. Third item",
                "And some text after."
            ],
        )
        
    def test_mixed_content(self):
        """Test a mix of different markdown elements"""
        md = """# Main Title

Introduction paragraph with **bold** and _italic_ text.

## Subsection

- List item 1
- List item 2

> Important quote
> On multiple lines

```
code block
```"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Main Title",
                "Introduction paragraph with **bold** and _italic_ text.",
                "## Subsection",
                "- List item 1\n- List item 2",
                "> Important quote\n> On multiple lines",
                "```\ncode block\n```"
            ],
        )