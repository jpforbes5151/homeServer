import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.example.com"})
        props_html = node.props_to_html()
        self.assertEqual(props_html, ' href="https://www.example.com"')

    def test_props_to_html_without_props(self):
        node = HTMLNode(tag="div", value="This is a div")
        props_html = node.props_to_html()
        self.assertEqual(props_html, '')
    
class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_without_tag(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_to_html_without_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("b", "Bold text")])

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", [])

    def test_nested_parent_nodes(self):
        inner_node = ParentNode(
            "span",
            [
                LeafNode(None, "Inner text"),
                LeafNode("b", "Bold inner text"),
            ]
        )
        outer_node = ParentNode("div", [inner_node])
        self.assertEqual(
            outer_node.to_html(),
            "<div><span>Inner text<b>Bold inner text</b></span></div>"
        )

if __name__ == "__main__":
    unittest.main()

# Example usage:
# node = HTMLNode(tag="p", value="This is a paragraph", props={"class": "highlight"})
# print(node.tag)  # Output: p
# print(node.value)  # Output: This is a paragraph
# print(node.children)  # Output: []
# print(node.props)  # Output: {'class': 'highlight'}
# print(node.props_to_html())  # Output: ' class="highlight"'