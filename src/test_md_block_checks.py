from mdblocks import BlockType, block_to_blocktype

import unittest


class TestTextNode(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_blocktype("Simple string with some text anod nothing more"),
        )

    def test_heading(self):
        self.assertEqual(BlockType.HEADING, block_to_blocktype("## test heading"))

    def test_codeblock(self):
        self.assertEqual(
            BlockType.CODE,
            block_to_blocktype("""```
print("Hello World!")
        """),
        )

    def test_quote(self):
        self.assertEqual(BlockType.QUOTE, block_to_blocktype("> this is a quote block"))

    def test_unordered_list(self):
        self.assertEqual(
            BlockType.UNORDERED_LIST, block_to_blocktype("- List this item")
        )

    def test_ordered_list(self):
        self.assertEqual(
            BlockType.ORDERED_LIST, block_to_blocktype(". this is an ordered list item")
        )

    def test_spaceless_list(self):
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_blocktype(".text that is just starting with dot"),
        )


if __name__ == "__main__":
    unittest.main()
