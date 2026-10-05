from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "plaintext"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text #Text Content of the Node
        self.text_type: TextType = text_type
        self.url = url
    
    def __eq__(self,other: "TextNode") -> bool:
        is_text = self.text == other.text
        is_text_type = self.text_type == other.text_type
        is_url = self.url == other.url
        return (is_text and is_text_type and is_url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None,value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b",value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i",value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code",value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img",value="",props={"src": text_node.url,"alt": text_node.text})
        case _:
            raise Exception("Text Type NOT valid for given TextNode")

