import unittest

from textnode import TextNode, TextType
from converter import split_nodes_delimeter


class TestTextNode(unittest.TestCase):
    def test_text_with_code(self):
        node = TextNode("This is a `CODE_BLOCK` text node", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.PLAIN_TEXT),
                TextNode("CODE_BLOCK", TextType.CODE_TEXT),
                TextNode(" text node", TextType.PLAIN_TEXT),
            ],
        )

    def test_text_with_multy_code(self):
        node = TextNode(
            "This is a `FIRST_BLOCK``SECOND_BLOCK` text node", TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.PLAIN_TEXT),
                TextNode("FIRST_BLOCK", TextType.CODE_TEXT),
                TextNode("SECOND_BLOCK", TextType.CODE_TEXT),
                TextNode(" text node", TextType.PLAIN_TEXT),
            ],
        )

    def test_text_with_bold(self):
        node = TextNode("This is a **BOLD_BLOCK** text node", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.PLAIN_TEXT),
                TextNode("BOLD_BLOCK", TextType.BOLD_TEXT),
                TextNode(" text node", TextType.PLAIN_TEXT),
            ],
        )

    def test_text_with_italic(self):
        node = TextNode("This is a _ITALICBLOCK_ text node", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimeter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.PLAIN_TEXT),
                TextNode("ITALICBLOCK", TextType.ITALIC_TEXT),
                TextNode(" text node", TextType.PLAIN_TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
