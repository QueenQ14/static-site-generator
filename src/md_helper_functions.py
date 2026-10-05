import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    delimiter = "\n\n"
    blocks = markdown.split(delimiter)
    blocks = list(map(lambda x: x.strip(),blocks))
    blocks = list(filter(lambda x: x != "",blocks))
    return blocks

def block_to_block_type(block: str) -> BlockType:
    heading_pattern = r"^(#{1,6})\s\w+"
    if re.findall(heading_pattern,block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    is_quote = True
    is_unordered = True
    is_ordered = True
    lines = block.split('\n')
    for i in range(len(lines)):
        if not lines[i].startswith(">"):
            is_quote = False
        if not lines[i].startswith("- "):
            is_unordered = False
        if not lines[i].startswith(f"{i+1}. "):
            is_ordered = False
    if is_quote:
        return BlockType.QUOTE
    if is_unordered:
        return BlockType.ULIST
    if is_ordered:
        return BlockType.OLIST   
    return BlockType.PARAGRAPH