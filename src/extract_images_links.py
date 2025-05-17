import re
from textnode import *


def extract_markdown_images(text):
    out = []
    #IMAGE = "![alt text](url)"
    alt_texts = re.findall(r"!\[(.*?)\]", text)
    url_texts = re.findall(r"\((.*?)\)", text)

    for i in range(0, len(alt_texts)):
        out.append((alt_texts[i], url_texts[i]))
    return out

def extract_markdown_links(text):
    out = []
    #LINK = "[anchor text](url)" but not "![alt text](url)"
    # Get all patterns like [text] that are not preceded by !
    anchor_texts = re.findall(r"(?<!!)\[(.*?)\]", text)
    # We need to find matching URLs for these anchor texts
    # First find all pairs of [text](url) that are not preceded by !
    pairs = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    
    return pairs

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]