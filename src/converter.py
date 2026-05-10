from htmlnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError("TextType not in the range of known values")
    if text_node.text_type == TextType.PLAIN_TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK_TEXT:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE_TEXT:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
