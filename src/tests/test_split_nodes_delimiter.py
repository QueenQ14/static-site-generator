import unittest
from nodes.textnode import TextNode, TextType
from functions.helper_functions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_multiple_blocks(self):
        node = TextNode("This `is` multiple `blocks`!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.CODE),
            TextNode(" multiple ", TextType.TEXT),
            TextNode("blocks", TextType.CODE),
            TextNode("!", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_missing_closing_delimiter(self):
        node = TextNode("This has an `unclosed block", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_no_delimiters_present(self):
        node = TextNode("Just a normal text string.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Just a normal text string.", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_starts_and_ends_with_delimiter(self):
        node = TextNode("`code at start and end`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("code at start and end", TextType.CODE)
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
