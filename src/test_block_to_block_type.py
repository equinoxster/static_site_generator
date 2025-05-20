import unittest

from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    
    # Heading Tests
    def test_heading_one(self):
        block = "# This is a heading 1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)
    
    def test_heading_six(self):
        block = "###### This is a heading 6"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)
    
    def test_heading_without_space(self):
        block = "##This should still be a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)
    
    # Code Block Tests
    def test_code_block_simple(self):
        block = "```\nprint('Hello World')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)
    
    def test_code_block_with_language(self):
        block = "```python\nprint('Hello World')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)
    
    def test_code_block_with_multiple_lines(self):
        block = "```\nline 1\nline 2\nline 3\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)
    
    # Quote Tests
    def test_quote_single_line(self):
        block = "> This is a quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)
    
    def test_quote_multiple_lines(self):
        block = "> Line 1\n> Line 2\n> Line 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)
    
    def test_quote_with_one_invalid_line(self):
        block = "> Line 1\nThis is not a quote\n> Line 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    # Unordered List Tests
    def test_unordered_list_single_item(self):
        block = "- Item 1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
    
    def test_unordered_list_multiple_items(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
    
    def test_unordered_list_with_one_invalid_item(self):
        block = "- Item 1\nThis is not an item\n- Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    # Ordered List Tests
    def test_ordered_list_single_item(self):
        block = "1. Item 1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)
    
    def test_ordered_list_multiple_items(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)
    
    def test_ordered_list_non_sequential_numbers(self):
        block = "1. Item 1\n5. Item 2\n10. Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)
    
    def test_ordered_list_with_one_invalid_item(self):
        block = "1. Item 1\nThis is not an item\n3. Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    # Paragraph Tests
    def test_paragraph_simple(self):
        block = "This is a simple paragraph."
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_paragraph_multiple_lines(self):
        block = "This is line 1.\nThis is line 2.\nThis is line 3."
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    # Edge Cases
    def test_empty_string(self):
        block = ""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_only_spaces(self):
        block = "   "
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_newlines_only(self):
        block = "\n\n\n"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    # Mixed Content (should default to paragraph)
    def test_mixed_content(self):
        block = "- Item 1\n> Quote\n1. Ordered item"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
