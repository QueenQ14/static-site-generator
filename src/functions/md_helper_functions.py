import re
from enum import Enum
from nodes.htmlnode import *
from functions.helper_functions import *
from nodes.textnode import *

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

def markdown_to_html_node(markdown: str):
    md_blocks = markdown_to_blocks(markdown)
    parent_blocks = []
    for block in md_blocks:
        parent_block = block_to_parent_node(block)
        parent_blocks.append(parent_block)
    
    return ParentNode(tag="div",children=parent_blocks)

def block_to_parent_node(block: str):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            clean_block = block.replace("\n", " ")
            children = text_to_children(clean_block)
            return ParentNode(tag="p",children=children)
        case BlockType.HEADING:
            count = len(block) - len(block.lstrip('#'))
            clean_block = block.lstrip('#')
            clean_block = clean_block.lstrip()
            children = text_to_children(clean_block)
            return ParentNode(tag=f"h{count}",children=children)
        case BlockType.QUOTE:
            clean_lines = []
            for line in block.split("\n"):
                clean_line = line.lstrip("> ")
                clean_lines.append(clean_line)
            cleaned_line = "\n".join(clean_lines)
            children = text_to_children(cleaned_line)
            return ParentNode(tag="blockquote",children=children)
        case BlockType.ULIST:
            list_items = []
            for line in block.split("\n"):
                clean_line = line[2:]
                line_children = text_to_children(clean_line)
                line_node = ParentNode(tag="li",children=line_children)
                list_items.append(line_node) 
            return ParentNode(tag="ul",children=list_items)
        case BlockType.OLIST:
            list_items = []
            for line in block.split("\n"):
                clean_line = line.split(". ",1)[1]
                line_children = text_to_children(clean_line)
                line_node = ParentNode(tag="li",children=line_children)
                list_items.append(line_node) 
            return ParentNode(tag="ol",children=list_items)
        case BlockType.CODE:
            clean_block = block.strip("`").lstrip("\n")
            code_block = TextNode(clean_block,TextType.CODE)
            html_code = text_node_to_html_node(code_block)
            return ParentNode(tag="pre",children=[html_code])


def text_to_children(block: str):
    text_nodes = text_to_textnodes(block)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children
