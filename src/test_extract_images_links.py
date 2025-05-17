import unittest
from extract_images_links import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_no_images(self):
        text = "This is text with no images"
        self.assertEqual(extract_markdown_images(text), [])
        
    def test_extract_one_image(self):
        text = "This is text with an image ![alt text](image.png)"
        self.assertEqual(extract_markdown_images(text), [("alt text", "image.png")])
        
    def test_extract_two_images(self):
        text = "This is text with two images ![first alt](first.jpg) and ![second alt](second.png)"
        self.assertEqual(extract_markdown_images(text), [("first alt", "first.jpg"), ("second alt", "second.png")])
        
    def test_extract_three_images(self):
        text = "Three images: ![img1](url1.jpg) middle text ![img2](url2.png) more text ![img3](url3.gif)"
        self.assertEqual(extract_markdown_images(text), [("img1", "url1.jpg"), ("img2", "url2.png"), ("img3", "url3.gif")])
    
    def test_image_with_empty_alt_text(self):
        text = "Image with empty alt text: ![](empty.jpg)"
        self.assertEqual(extract_markdown_images(text), [("", "empty.jpg")])


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_no_links(self):
        text = "This is text with no links"
        self.assertEqual(extract_markdown_links(text), [])
        
    def test_extract_one_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev")])
        
    def test_extract_two_links(self):
        text = "This is text with links [first link](https://first.com) and [second link](https://second.com)"
        self.assertEqual(extract_markdown_links(text), [("first link", "https://first.com"), ("second link", "https://second.com")])
        
    def test_extract_three_links(self):
        text = "Three links: [link1](url1.com) middle text [link2](url2.com) more text [link3](url3.com)"
        self.assertEqual(extract_markdown_links(text), [("link1", "url1.com"), ("link2", "url2.com"), ("link3", "url3.com")])
    
    def test_link_with_empty_anchor_text(self):
        text = "Link with empty anchor text: [](empty.com)"
        self.assertEqual(extract_markdown_links(text), [("", "empty.com")])
    
    def test_mixed_content(self):
        text = "This has a ![image](img.jpg) and a [link](https://link.com) mixed together"
        # Only extract links in this test
        self.assertEqual(extract_markdown_links(text), [("link", "https://link.com")])


if __name__ == "__main__":
    unittest.main()
