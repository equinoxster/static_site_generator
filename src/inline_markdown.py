from htmlnode import *
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        nodes_new_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter)%2 != 0:
            raise Exception(f"invalid markdown in node {node.__repr__()}")

        start_with_delimiter = node.text.startswith(delimiter)
        split_node_text = node.text.split(delimiter)

        # Handle text based on whether it starts with a delimiter
        if start_with_delimiter:
            # First element is empty string, skip it and adjust the rest
            split_node_text = split_node_text[1:]
            # Now the first element should be the first special text segment
            for i in range(0, len(split_node_text)):
                if i%2 == 0:
                    # Only add non-empty nodes
                    if split_node_text[i]:
                        nodes_new_nodes.append(TextNode(split_node_text[i], text_type, node.url))
                else:
                    # Only add non-empty nodes
                    if split_node_text[i]:
                        nodes_new_nodes.append(TextNode(split_node_text[i], TextType.TEXT, node.url))
        else:
            # Normal case - alternate between regular text and special text
            for i in range(0, len(split_node_text)):
                if i%2 == 0:
                    # Only add non-empty nodes
                    if split_node_text[i]:
                        nodes_new_nodes.append(TextNode(split_node_text[i], TextType.TEXT, node.url))
                else:
                    # Only add non-empty nodes
                    if split_node_text[i]:
                        nodes_new_nodes.append(TextNode(split_node_text[i], text_type, node.url))

        new_nodes.extend(nodes_new_nodes)

    return new_nodes
