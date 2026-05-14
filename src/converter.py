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
            raise Exception(f"missing closing delimeter in string '{node.text}'")
        for i in range(0, len(temp)):
            if i % 2 == 0 and len(temp[i]) != 0:
                new_nodes.append(TextNode(temp[i], node.text_type))
            elif i % 2 != 0:
                new_nodes.append(TextNode(temp[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
        else:
            current = node.text
            for image_alt, image_link in matches:
                if len(current) == 0:
                    continue
                sections = current.split(f"![{image_alt}]({image_link})", 1)
                current = sections[1]
                if len(sections[0]) != 0:
                    new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE_TEXT, image_link))
            if len(current) != 0:
                new_nodes.append(TextNode(current, TextType.PLAIN_TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
        else:
            current = node.text
            for link_alt, link_text in matches:
                # if len(current) == 0:
                #    continue
                sections = current.split(f"[{link_alt}]({link_text})", 1)
                current = sections[1]
                if len(sections[0]) != 0:
                    new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
                new_nodes.append(TextNode(link_alt, TextType.LINK_TEXT, link_text))
            if len(current) != 0:
                new_nodes.append(TextNode(current, TextType.PLAIN_TEXT))
    return new_nodes


def text_to_textnodes(text):
    result_nodes = split_nodes_delimeter(
        [TextNode(text, TextType.PLAIN_TEXT)], "`", TextType.CODE_TEXT
    )
    result_nodes = split_nodes_delimeter(result_nodes, "**", TextType.BOLD_TEXT)
    result_nodes = split_nodes_delimeter(result_nodes, "_", TextType.ITALIC_TEXT)
    result_nodes = split_nodes_image(result_nodes)
    result_nodes = split_nodes_link(result_nodes)
    return result_nodes
