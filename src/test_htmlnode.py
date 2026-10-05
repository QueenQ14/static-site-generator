import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        #Testing two empty HTMLNodes
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_eq_a(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
            }
        )
        node2 = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
            }
        )
        #Equal nodes
        #Should print the same props_to_html() value
        self.assertEqual(node.props_to_html(),node2.props_to_html())
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_not_eq(self):
        #Almost equal nodes but props are different
        node = HTMLNode(tag="h1",value="meow",props={"href": "https://boot.dev"})
        node2 = HTMLNode(tag="h1",value="woof",props={"target": "_blank"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello", children=None, props={"class": "paragraph"})
        self.assertEqual(repr(node), "HTMLNode(p, Hello, children: None, {'class': 'paragraph'})")

if __name__ == "__main__":
    unittest.main()