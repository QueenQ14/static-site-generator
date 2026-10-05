from nodes.textnode import *
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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    list_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            list_nodes.append(node)
            continue        
        original_text = node.text
        matches = extract_markdown_images(node.text)
        for match in matches:
            image_alt = match[0]
            image_link = match[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_node = TextNode(sections[0],TextType.TEXT)
                list_nodes.append(new_node)
            image_node = TextNode(image_alt,TextType.IMAGE,image_link)
            list_nodes.append(image_node)
            original_text = sections[1]
        if original_text == "":
            continue
        list_nodes.append(TextNode(original_text,TextType.TEXT))
    
    return list_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    list_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            list_nodes.append(node)
            continue        
        original_text = node.text
        matches = extract_markdown_links(node.text)
        for match in matches:
            link_text = match[0]
            link_url = match[1]
            sections = original_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0] != "":
                new_node = TextNode(sections[0],TextType.TEXT)
                list_nodes.append(new_node)
            link_node = TextNode(link_text,TextType.LINK,link_url)
            list_nodes.append(link_node)
            original_text = sections[1]
        if original_text == "":
            continue
        list_nodes.append(TextNode(original_text,TextType.TEXT))
    
    return list_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text,TextType.TEXT)
    nodes = split_nodes_delimiter([node,],"_",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes