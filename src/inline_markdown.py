from htmlnode import *
from textnode import *
from extract_images_links import *



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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        nodes_new_nodes =[]
        node_text = node.text
        image_tuples = extract_markdown_images(node.text)
        if len(image_tuples) == 0:
            new_nodes.append(node)
            continue

        for one_tuple in image_tuples:
            tuple_in_markdown = f"![{one_tuple[0]}]({one_tuple[1]})"
            split_text = node_text.split(tuple_in_markdown,1)

            if split_text[0] == "": # text starts with image
                node_text = split_text[1]
                nodes_new_nodes.append(TextNode(one_tuple[0], TextType.IMAGE, one_tuple[1]))                
            elif split_text[len(split_text) - 1] == "": # text ends with image. this means are on the last value of the tuple
                nodes_new_nodes.append(TextNode(split_text[0], TextType.TEXT, node.url))
                nodes_new_nodes.append(TextNode(one_tuple[0], TextType.IMAGE, one_tuple[1]))
                node_text = ""
            elif split_text[0] == "" and split_text[1] == "": # text is oly the image
                nodes_new_nodes.append(TextNode(one_tuple[0], TextType.IMAGE, one_tuple[1]))
                node_text = "" #it should be this if we get here
            else:
                nodes_new_nodes.append(TextNode(split_text[0], TextType.TEXT, node.url))                
                nodes_new_nodes.append(TextNode(one_tuple[0], TextType.IMAGE, one_tuple[1]))
                node_text = split_text[1]


        if len(node_text) > 0:
            nodes_new_nodes.append(TextNode(node_text, TextType.TEXT, node.url))

        new_nodes.extend(nodes_new_nodes)
    return new_nodes
