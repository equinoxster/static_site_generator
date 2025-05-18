from textnode import *
from inline_markdown import *

def text_to_textnode(text):

    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    #print(f"1. {nodes}")
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    #print(f"2. {nodes}")
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    #print(f"3. {nodes}")
    nodes = split_nodes_image(nodes)
    #print(f"4. {nodes}")
    nodes = split_nodes_link(nodes)

    return nodes


