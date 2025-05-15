

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        out = ""
        for key in self.props.keys():
            out += f" {key}=\"{self.props[key]}\""
        return out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        
        if self.tag == None:
            return f"{self.value}"
        
        if self.props == None or len(self.props) == 0:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:    
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag==None or tag=="":
            raise ValueError("Tag is required")
        if children == None:
            raise ValueError("Children value is invalid")
        super().__init__(tag, None, children, props)

    def to_html(self):
        html_string = ""
        if self.props == None or len(self.props) == 0:
            html_string += f"<{self.tag}>"
        else:    
            html_string += f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:            
            html_string += child.to_html()
                    
        
        html_string += f"</{self.tag}>"
        return html_string
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

