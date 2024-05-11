class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children='{self.children}', props='{self.props}')"

    def to_html(self):
        raise NotImplementedError("to_html method not implemented yet")
    
    def props_to_html(self):
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)
        if value is None:
            raise ValueError("LeafNode must have a value.")

    def to_html(self):
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("A Parent Node must have a tag.")
        
        if not children:
            raise ValueError("A Parent Node object must have at least one child.")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.children:
            raise ValueError("A Parent Node object must have at least one child.")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html