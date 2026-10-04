from enum import Enum

class TextType(Enum):
    PLAIN = "plaintext"
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