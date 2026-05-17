import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_tag_val(self):
        node = HTMLNode("TestTag", "TestValue", ["test1", "test2"], {"test": "dict"})
        self.assertEqual(node.tag, "TestTag")

    def test_val(self):
        node = HTMLNode("TestTag", "TestValue", ["test1", "test2"], {"test": "dict"})
        self.assertEqual(node.value, "TestValue")

    def test_children_value(self):
        node = HTMLNode("TestTag", "TestValue", ["test1", "test2"], {"test": "dict"})
        self.assertEqual(node.children, ["test1", "test2"])

    def test_props_to_html(self):
        node = HTMLNode("TestTag", "TestValue", ["test1", "test2"], {"test": "dict"})
        self.assertEqual(node.props_to_html(), ' test="dict"')

    def test_props(self):
        node = HTMLNode("TestTag", "TestValue", ["test1", "test2"], {"test": "dict"})
        self.assertEqual(node.props, {"test": "dict"})


if __name__ == "__main__":
    unittest.main()
