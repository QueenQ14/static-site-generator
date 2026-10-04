import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Heading!")
        self.assertEqual(node.to_html(), "<h1>Heading!</h1>")

    def test_leaf_to_html_value_not_match(self):
        node = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<p>Hello, Juicewrld!</p>")

    def test_leaf_to_html_raise_valueerror(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tags(self):    
        node = LeafNode(None,"im just a value bro")
        self.assertEqual(node.to_html(), "im just a value bro")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("p", "Hello, world!",{"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<p href="https://boot.dev">Hello, world!</p>')

    def test_repr(self):
        node = LeafNode("p", "Hello, world!", {"href": "https://boot.dev"})
        self.assertEqual(repr(node), "LeafNode(p, Hello, world!, {'href': 'https://boot.dev'})")

if __name__ == "__main__":
    unittest.main()