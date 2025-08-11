from htmlnode import *
from extract_markdown_blocks import *
from block_to_block_type import *
from text_to_textnodes import *
from inline_markdown import *
from textnode import *
import re



def markdown_to_html_node(markdown):
    # Extract blocks from markdown
    blocks = markdown_to_blocks(markdown)
    
    # Convert each block to HTML nodes
    html_nodes = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            # For paragraphs, convert inline markdown and wrap in <p> tag
            # Replace newlines and normalize whitespace for paragraph text
            paragraph_text = ' '.join(block.split())
            text_nodes = text_to_textnode(paragraph_text)
            leaf_nodes = [text_node_to_html_node(node) for node in text_nodes]
            paragraph_node = ParentNode("p", leaf_nodes)
            html_nodes.append(paragraph_node)
            
        elif block_type == BlockType.CODE:
            # For code blocks, extract the content between ``` and wrap in <pre><code>
            lines = block.split('\n')
            # Remove the opening and closing ```
            code_lines = lines[1:-1]
            # Strip common leading whitespace from all lines
            if code_lines:
                # Find minimum indentation (excluding empty lines)
                non_empty_lines = [line for line in code_lines if line.strip()]
                if non_empty_lines:
                    min_indent = min(len(line) - len(line.lstrip()) for line in non_empty_lines)
                    # Remove the common indentation from all lines
                    code_lines = [line[min_indent:] if len(line) >= min_indent else line for line in code_lines]
            code_content = '\n'.join(code_lines)
            # Add trailing newline to match expected output, or ensure at least one newline for empty blocks
            if not code_content:
                code_content = '\n'
            elif not code_content.endswith('\n'):
                code_content += '\n'
            code_node = LeafNode("code", code_content)
            pre_node = ParentNode("pre", [code_node])
            html_nodes.append(pre_node)
            
        elif block_type == BlockType.HEADING:
            # For headings, determine level and convert inline markdown
            level = 0
            for char in block:
                if char == '#':
                    level += 1
                else:
                    break
            
            heading_text = block[level:].strip()
            text_nodes = text_to_textnode(heading_text)
            leaf_nodes = [text_node_to_html_node(node) for node in text_nodes]
            heading_node = ParentNode(f"h{level}", leaf_nodes)
            html_nodes.append(heading_node)
            
        elif block_type == BlockType.QUOTE:
            # For quotes, remove > from each line and convert inline markdown
            lines = block.split('\n')
            quote_lines = [line[1:].strip() for line in lines]
            quote_text = ' '.join(quote_lines)
            text_nodes = text_to_textnode(quote_text)
            leaf_nodes = [text_node_to_html_node(node) for node in text_nodes]
            quote_node = ParentNode("blockquote", leaf_nodes)
            html_nodes.append(quote_node)
            
        elif block_type == BlockType.UNORDERED_LIST:
            # For unordered lists, create <ul> with <li> items
            lines = block.split('\n')
            list_items = []
            for line in lines:
                item_text = line[2:].strip()  # Remove "- "
                text_nodes = text_to_textnode(item_text)
                leaf_nodes = [text_node_to_html_node(node) for node in text_nodes]
                li_node = ParentNode("li", leaf_nodes)
                list_items.append(li_node)
            ul_node = ParentNode("ul", list_items)
            html_nodes.append(ul_node)
            
        elif block_type == BlockType.ORDERED_LIST:
            # For ordered lists, create <ol> with <li> items
            lines = block.split('\n')
            list_items = []
            for line in lines:
                # Remove the number and period at the beginning
                import re
                item_text = re.sub(r'^\d+\. ', '', line)
                text_nodes = text_to_textnode(item_text)
                leaf_nodes = [text_node_to_html_node(node) for node in text_nodes]
                li_node = ParentNode("li", leaf_nodes)
                list_items.append(li_node)
            ol_node = ParentNode("ol", list_items)
            html_nodes.append(ol_node)
    
    # Wrap all HTML nodes in a div
    return ParentNode("div", html_nodes)
