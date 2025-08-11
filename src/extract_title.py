def extract_title(markdown: str) -> str:
    """
    Extract the H1 title from a markdown document.

    Rules:
    - Find the first line that starts with exactly one '#'.
    - Return the rest of the line with the leading '#' removed and whitespace trimmed.
    - If no H1 header exists, raise a ValueError.
    """
    if markdown is None:
        raise ValueError("No H1 title found")

    for line in markdown.splitlines():
        if line.startswith("#") and not line.startswith("##"):
            # Strip a single leading '#', then trim whitespace
            return line[1:].strip()

    raise ValueError("No H1 title found")
