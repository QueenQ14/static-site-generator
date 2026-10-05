import unittest
from textnode import TextNode, TextType
from helper_functions import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes_comprehensive(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(nodes, expected)

    def test_text_to_textnodes_plain_text(self):
        text = "Just a totally normal sentence."
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Just a totally normal sentence.", TextType.TEXT)
        ]
        self.assertListEqual(nodes, expected)

    def test_text_to_textnodes_multiple_same_type(self):
        text = "**bold one** and **bold two**"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("bold one", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold two", TextType.BOLD),
        ]
        self.assertListEqual(nodes, expected)

    def test_text_to_textnodes_consecutive_types(self):
        text = "![image](url)[link](url2)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("image", TextType.IMAGE, "url"),
            TextNode("link", TextType.LINK, "url2"),
        ]
        self.assertListEqual(nodes, expected)

    def test_text_to_textnodes_nested_trick(self):
        # Text to textnodes splits sequentially, so it should handle multiple different types intermixed cleanly
        text = "Start _italic_ middle `code` end"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" middle ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertListEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()
