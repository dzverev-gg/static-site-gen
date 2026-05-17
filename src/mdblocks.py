import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_blocktype(block: str) -> BlockType:
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```\n"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    if all(re.match(r"^\d+\. ", line) for line in block.split("\n")):
        level = 1
        ordered = True
        for line in block.split("\n"):
            if line.startswith(f"{level}"):
                level += 1
            else:
                ordered = False
        if ordered:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    splitted = markdown.split("\n\n")
    result: list[str] = []
    for line in splitted:
        if len(line.strip()) != 0:
            result.append(line.strip())
    return result
