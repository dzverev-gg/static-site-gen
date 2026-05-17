import unittest

from converter import extract_markdown_images, extract_markdown_links


class TestTextExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/index.html)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/index.html")], matches)

    def test_extract_image_only(self):
        matches = extract_markdown_images(
            "This is a text with ![image](https://i.imgur.com/zjjcJKZ.png) and [link](https://google.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_links_only(self):
        matches = extract_markdown_links(
            "This is a text with ![image](https://i.imgur.com/zjjcJKZ.png) and [link](https://google.com)"
        )
        self.assertListEqual([("link", "https://google.com")], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "This is a text with ![image](https://i.imgur.com/zjjcJKZ.png) and ![link](https://google.com)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("link", "https://google.com"),
            ],
            matches,
        )

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "This is a text with [image](https://i.imgur.com/zjjcJKZ.png) and [link](https://google.com)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("link", "https://google.com"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()
