import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Test",TextType.ITALIC_TEXT, "url")
        self.assertEqual(repr(node), 'TextNode(Test, italic, url)')

    def test_diff_url(self):
        node = TextNode("Test",TextType.IMAGE_TEXT)
        node2 = TextNode("Test",TextType.IMAGE_TEXT, "url")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("TEst",TextType.BOLD_TEXT)
        self.assertEqual(node.url, None)

    def test_diff_style(self):
        node = TextNode("Test",TextType.PLAIN_TEXT, "url")
        node2 = TextNode("Test",TextType.IMAGE_TEXT, "url")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
