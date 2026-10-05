from textnode import *
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    list_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            list_nodes.append(node)
            continue
        if delimiter == None:
            raise Exception("Delimiter was NOT provided.")
        
        split_text = node.text.split(delimiter)
        if len(split_text)%2 == 0:
            raise Exception(f"Found no matching closing delimiter: {delimiter}")
        
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i%2 == 0:
                list_nodes.append(TextNode(split_text[i],TextType.TEXT))
            else:
                list_nodes.append(TextNode(split_text[i],text_type))

    return list_nodes

def extract_markdown_images(text: str) -> list[tuple[str]]:
    # matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text: str) -> list[tuple[str]]:
    # matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches