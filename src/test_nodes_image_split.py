import unittest

from textnode import TextNode, TextType
from converter import split_nodes_image


class TestTextNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode(
                    "image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"
                ),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE_TEXT,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    def test_split_multiple_images(self):
        nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.PLAIN_TEXT,
            ),
            TextNode(
                "This is a second text with an ![third image](https://i.imgur.com/image.png)",
                TextType.PLAIN_TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode(
                    "image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"
                ),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE_TEXT,
                    "https://i.imgur.com/3elNhQu.png",
                ),
                TextNode("This is a second text with an ", TextType.PLAIN_TEXT),
                TextNode(
                    "third image", TextType.IMAGE_TEXT, "https://i.imgur.com/image.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_and_links(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and a link [link](https://google.com)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode(
                    "image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"
                ),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE_TEXT,
                    "https://i.imgur.com/3elNhQu.png",
                ),
                TextNode(" and a link [link](https://google.com)", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
