import unittest
from functions.md_helper_functions import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = "# This is a **bolded** heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a <b>bolded</b> heading</h1></div>",
        )

    def test_quote(self):
        md = "> This is a\n> blockquote block\n> with _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a\nblockquote block\nwith <i>italic</i> text</blockquote></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings_different_levels(self):
        md = """
# Heading 1

## Heading 2

###### Heading 6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h6>Heading 6</h6></div>",
        )

    def test_empty(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

    def test_paragraph_with_links(self):
        md = "This is a paragraph with a [link](https://boot.dev)."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with a <a href=\"https://boot.dev\">link</a>.</p></div>",
        )

    def test_paragraph_with_images(self):
        md = "Here is an image ![alt text](https://image.url)."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Here is an image <img src=\"https://image.url\" alt=\"alt text\"></img>.</p></div>",
        )

    def test_unordered_list_nested_formatting(self):
        md = """
- **bold** and _italic_
- `code` and [link](url)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li><b>bold</b> and <i>italic</i></li><li><code>code</code> and <a href=\"url\">link</a></li></ul></div>",
        )

    def test_ordered_list_multidigit(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
4. Item 4
5. Item 5
6. Item 6
7. Item 7
8. Item 8
9. Item 9
10. Item 10
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li><li>Item 4</li><li>Item 5</li><li>Item 6</li><li>Item 7</li><li>Item 8</li><li>Item 9</li><li>Item 10</li></ol></div>",
        )

    def test_mixed_code_and_lists(self):
        md = """
```
print("hello")
```

- list item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>print(\"hello\")\n</code></pre><ul><li>list item</li></ul></div>",
        )

    def test_multiple_paragraphs(self):
        md = """
Paragraph 1

Paragraph 2


Paragraph 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Paragraph 1</p><p>Paragraph 2</p><p>Paragraph 3</p></div>",
        )

    def test_quote_with_newlines(self):
        md = "> Quote line 1\n> Quote line 2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote line 1\nQuote line 2</blockquote></div>",
        )

    def test_complex_document(self):
        md = """
# Welcome

This is a totally _awesome_ document.

- It has lists
- It has **bold** text

> And even a quote!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Welcome</h1><p>This is a totally <i>awesome</i> document.</p><ul><li>It has lists</li><li>It has <b>bold</b> text</li></ul><blockquote>And even a quote!</blockquote></div>",
        )

if __name__ == "__main__":
    unittest.main()
