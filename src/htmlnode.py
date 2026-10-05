class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children: list[HTMLNode] = children
        self.props: dict = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        res = ""
        for key in self.props:
            res += f' {key}="{self.props[key]}"'
        return res
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag=tag,value=value,props=props,children=None)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Error: Leaf nodes MUST have a value.")
        if self.tag == None:
            return str(self.value)
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag,value=None,children=children,props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Error: Please set 'tag' for ParentNode")
        if self.children == None:
            raise ValueError("Error: Children is missing for ParentNode")
        res = ""
        for node in self.children:
            res += f"{node.to_html()}"
        
        return f"<{self.tag}{self.props_to_html()}>{res}</{self.tag}>"


