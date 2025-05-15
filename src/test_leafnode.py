import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        # Test with tag, value and props
        node = LeafNode("div", "content", {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "content")
        self.assertIsNone(node.children)  # LeafNodes always have children=None
        self.assertEqual(node.props, {"class": "container"})
        
        # Test with default parameters
        default_node = LeafNode()
        self.assertIsNone(default_node.tag)
        self.assertIsNone(default_node.value)
        self.assertIsNone(default_node.children)
        self.assertIsNone(default_node.props)
    
    def test_to_html_with_tag_and_value(self):
        # Test normal case with tag and value
        node = LeafNode("p", "Hello, world!", {"class": "text"})
        expected_html = '<p class="text">Hello, world!</p>'
        self.assertEqual(node.to_html(), expected_html)
        
        # Test without props
        node_no_props = LeafNode("span", "Simple text")
        self.assertEqual(node_no_props.to_html(), "<span>Simple text</span>")
    
    def test_to_html_without_tag(self):
        # Test case where tag is None
        node = LeafNode(None, "Plain text")
        self.assertEqual(node.to_html(), "Plain text")
    
    def test_to_html_raises_value_error(self):
        # Test that ValueError is raised for empty or None value
        node_empty_value = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node_empty_value.to_html()
            
        node_none_value = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node_none_value.to_html()
    
    def test_props_to_html(self):
        # Test with multiple properties
        node = LeafNode("div", "content", {"class": "container", "id": "main"})
        html = node.to_html()
        self.assertIn('class="container"', html)
        self.assertIn('id="main"', html)
        
        # Test with single property
        node_single_prop = LeafNode("span", "text", {"style": "color: red;"})
        html_single_prop = node_single_prop.to_html()
        self.assertIn('style="color: red;"', html_single_prop)

if __name__ == "__main__":
    unittest.main()
