import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_h1_with_spaces(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_ignores_h2_and_below(self):
        with self.assertRaises(ValueError):
            extract_title("## Not a title")

    def test_finds_first_h1_in_document(self):
        md = """
Intro paragraph
# First Title
## Subtitle
# Second Title
""".strip()
        self.assertEqual(extract_title(md), "First Title")

    def test_no_h1_raises(self):
        with self.assertRaises(ValueError):
            extract_title("No headings here\nAnother line")

if __name__ == "__main__":
    unittest.main()
