import unittest
from nodes.htmlnode import *


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_no_tag_raises_error(self):
        node = ParentNode(None, [LeafNode("b", "Bold")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children_raises_error(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_nested_parents(self):
        child = ParentNode("span", [LeafNode("i", "italic")])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span><i>italic</i></span></div>")

    def test_mixed_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode("span", [LeafNode("b", "bold")]),
                LeafNode("i", "italic")
            ]
        )
        self.assertEqual(node.to_html(), "<div><span><b>bold</b></span><i>italic</i></div>")

    def test_deeply_nested_parents(self):
        level_3 = ParentNode("div", [LeafNode("p", "deepest")])
        level_2 = ParentNode("section", [level_3])
        level_1 = ParentNode("main", [level_2])
        self.assertEqual(
            level_1.to_html(),
            "<main><section><div><p>deepest</p></div></section></main>"
        )

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("b", "bold")], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><b>bold</b></div>')

    def test_to_html_with_multiple_props(self):
        node = ParentNode("a", [LeafNode(None, "Click me")], {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev" target="_blank">Click me</a>')

    def test_repr(self):
        node = ParentNode("div", [LeafNode("b", "bold")], {"class": "container"})
        self.assertEqual(repr(node), "ParentNode(div, children: [LeafNode(b, bold, None)], {'class': 'container'})")

if __name__ == "__main__":
    unittest.main()