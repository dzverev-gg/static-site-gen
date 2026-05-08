

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method is not implemented yetself")



    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        props_string = ""
        for key in self.props.keys():
            props_string += f' {key}="{self.props[key]}"'
        return props_string


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        #self.tag = tag
        #self.value = value
        #self.props = props
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return self.value
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    


