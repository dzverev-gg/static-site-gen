import unittest

from textnode import TextNode, TextType
from converter import split_nodes_link


class TestTextNode(unittest.TestCase):
    def test_split_link(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/index.html) and another [second link](https://google.com)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK_TEXT, "https://i.imgur.com/index.html"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second link",
                    TextType.LINK_TEXT,
                    "https://google.com",
                ),
            ],
            new_nodes,
        )

    def test_split_multiple_images(self):
        nodes = [
            TextNode(
                "This is text with an [link](https://i.imgur.com/index.html) and another [second link](https://google.com)",
                TextType.PLAIN_TEXT,
            ),
            TextNode(
                "This is a second text with an [third link](https://i.imgur.com/image.png)",
                TextType.PLAIN_TEXT,
            ),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK_TEXT, "https://i.imgur.com/index.html"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second link",
                    TextType.LINK_TEXT,
                    "https://google.com",
                ),
                TextNode("This is a second text with an ", TextType.PLAIN_TEXT),
                TextNode(
                    "third link", TextType.LINK_TEXT, "https://i.imgur.com/image.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_and_links(self):
        node = TextNode(
            "This is text with an [link](https://google.com) and another [second link](https://yahoo.com) and an image ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK_TEXT, "https://google.com"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second link",
                    TextType.LINK_TEXT,
                    "https://yahoo.com",
                ),
                TextNode(
                    " and an image ![image](https://i.imgur.com/zjjcJKZ.png)",
                    TextType.PLAIN_TEXT,
                ),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
