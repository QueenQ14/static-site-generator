def markdown_to_blocks(markdown: str) -> list[str]:
    delimiter = "\n\n"
    blocks = markdown.split(delimiter)
    blocks = list(map(lambda x: x.strip(),blocks))
    blocks = list(filter(lambda x: x != "",blocks))
    return blocks