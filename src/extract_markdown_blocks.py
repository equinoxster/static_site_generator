

def markdown_to_blocks(text):
    blocks = text.split("\n\n")

    blocks_out = []
    for block in blocks:
        block = block.strip()
        if block.startswith("\n"):
            block.replace("\n", "", 1)
        if block == "\n" or block == "":
            continue
        blocks_out.append(block)
    

    return blocks_out