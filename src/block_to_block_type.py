from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered list"
    ORDERED_LIST = "Ordered list"

def block_to_block_type(block):
    if (re.match(r'^#{1,6}', block)):
        return BlockType.HEADING
    elif (re.match(r'^```{1,3}', block) and re.search(r'```$', block.splitlines()[-1])):
        return BlockType.CODE
    
    block_lines = block.split("\n")
    if (check_all_lines(block_lines, r'^>')):
        return BlockType.QUOTE
    elif check_all_lines(block_lines, r'^- '):
        return BlockType.UNORDERED_LIST
    elif check_all_lines(block_lines, r'^\d+. '):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def check_all_lines(lines, regex):

    for line in lines:
        if (not re.match(regex, line)):
            return False
    
    return True


