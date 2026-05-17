import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag_val(self):
        node = LeafNode("TestTag", "TestValue", {"test": "dict"})
        self.assertEqual(node.tag, "TestTag")

    def test_val(self):
        node = LeafNode("TestTag", "TestValue", {"test": "dict"})
        self.assertEqual(node.value, "TestValue")

    def test_props_to_html(self):
        node = LeafNode("TestTag", "TestValue", {"test": "dict"})
        self.assertEqual(node.props_to_html(), ' test="dict"')

    def test_props(self):
        node = LeafNode("TestTag", "TestValue", {"test": "dict"})
        self.assertEqual(node.props, {"test": "dict"})

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_href(self):
        node = LeafNode("p", "Hello, world!", {"href": "https://google.com"})
        self.assertEqual(
            node.to_html(), '<p href="https://google.com">Hello, world!</p>'
        )


if __name__ == "__main__":
    unittest.main()
