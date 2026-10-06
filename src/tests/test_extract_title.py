import unittest
from functions.md_helper_functions import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_strip_whitespace(self):
        self.assertEqual(extract_title("# Hello World   "), "Hello World")

    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("## Not a title")

    def test_multiple_blocks(self):
        markdown = """
Here is a paragraph.

# The Title

Here is another paragraph.
"""
        self.assertEqual(extract_title(markdown), "The Title")

if __name__ == '__main__':
    unittest.main()
