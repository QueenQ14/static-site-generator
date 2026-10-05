import unittest
from md_helper_functions import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        # 7 hashes is not a heading, it should be a paragraph
        self.assertEqual(block_to_block_type("####### Heading 7"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```\ndef hello():\n    print('hello')\n```"), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> line 1\n> line 2\n> line 3"), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        # Unordered lists can start with -
        self.assertEqual(block_to_block_type("- item 1\n- item 2"), BlockType.UNORDERED_LIST)
        # Unordered lists starting with * are not supported in this app
        self.assertEqual(block_to_block_type("* item 1\n* item 2"), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. item 1\n2. item 2\n3. item 3"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_invalid_ordered_list(self):
        # The numbers must increment exactly by 1 starting from 1
        self.assertEqual(block_to_block_type("1. item 1\n3. item 2"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("2. item 1\n3. item 2"), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("Just a completely normal paragraph without any special formatting."), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading_no_space(self):
        # Must have a space after the hashes
        self.assertEqual(block_to_block_type("#Heading"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code_missing_backticks(self):
        # Must have exactly 3 backticks
        self.assertEqual(block_to_block_type("``\ndef hello():\n    pass\n``"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code_inline(self):
        # Inline code is still just a paragraph block
        self.assertEqual(block_to_block_type("`code`"), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote_missing_bracket(self):
        # Every line must start with >
        self.assertEqual(block_to_block_type("> line 1\nline 2"), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_no_space(self):
        # Must have a space after the - or *
        self.assertEqual(block_to_block_type("-item 1\n-item 2"), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_mixed(self):
        # Mixed - and * fails because * is not supported
        self.assertEqual(block_to_block_type("- item 1\n* item 2"), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_no_space(self):
        # Must have a space after the dot
        self.assertEqual(block_to_block_type("1.item 1\n2.item 2"), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_wrong_start(self):
        # Must start exactly at 1
        self.assertEqual(block_to_block_type("3. item 1\n4. item 2"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
