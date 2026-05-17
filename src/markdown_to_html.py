import re
from converter import text_to_textnodes, text_node_to_html_node
from htmlnode import ParentNode, LeafNode, HTMLNode
from mdblocks import block_to_blocktype, markdown_to_blocks, BlockType
from textnode import TextType, TextNode


def markdown_to_html_node(markdown: str):
    splitted = markdown_to_blocks(markdown)
    html_nodes: list[HTMLNode] = []
    for block in splitted:
        type = block_to_blocktype(block)
        if type == BlockType.CODE:
            html_node = code_block_to_html_node(block)

        if type == BlockType.HEADING:
            level = block.index(" ")
            content = block[level + 1 :]
            html_node = ParentNode(f"h{level}", text_to_children(content))

        if type == BlockType.QUOTE:
            html_node = ParentNode("blockquote", text_to_children(block))

        if type == BlockType.PARAGRAPH:
            content = ""
            for line in block.split("\n"):
                content += line + " "
            html_node = ParentNode("p", text_to_children(content.strip()))

        if type == BlockType.UNORDERED_LIST:
            html_node = unordered_list_to_html_node(block)

        if type == BlockType.ORDERED_LIST:
            html_node = ordered_list_to_html_node(block)

        html_nodes.append(html_node)

    root = ParentNode("div", html_nodes)
    return root


def code_block_to_html_node(text: str):
    text = text.strip("`\n")
    node = TextNode(text + "\n", TextType.CODE_TEXT)
    return ParentNode("pre", [text_node_to_html_node(node)])


def unordered_list_to_html_node(text: str):
    list_nodes = []
    for line in text.split("- "):
        if len(line) > 0:
            node = ParentNode("li", text_to_children(line))
            list_nodes.append(node)
    return ParentNode("ul", list_nodes)


def ordered_list_to_html_node(text: str):
    list_nodes = []
    for line in re.split(r"\d+\. ", text):
        node = ParentNode("li", text_to_children(line))
        list_nodes.append(node)
    return ParentNode("ol", list_nodes)


def text_to_children(text: str):
    text_nodes: list[TextNode] = text_to_textnodes(text)
    html_nodes: list[LeafNode] = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
