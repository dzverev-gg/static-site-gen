from htmlnode import LeafNode
from textnode import TextType, TextNode
import re


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


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        temp = node.text.split(delimeter)
        if len(temp) % 2 == 0:
            raise Exception(f"missing closing delimeter in strin '{node.text}'")
        for i in range(0, len(temp)):
            if i % 2 == 0:
                new_nodes.append(TextNode(temp[i], node.text_type))
            else:
                new_nodes.append(TextNode(temp[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches
