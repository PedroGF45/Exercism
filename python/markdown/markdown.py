import re


def _parse_emphasis(text):
    """Parses bold (__) and italic (_) markup."""
    text = re.sub(r"__(.*?)__", r"<strong>\1</strong>", text)
    text = re.sub(r"_(.*?)_", r"<em>\1</em>", text)
    return text


def parse(markdown):
    lines = markdown.split("\n")
    html = ""
    in_list = False

    for line in lines:
        # Headers
        header_match = re.match(r"(#+) (.*)", line)
        if header_match and len(header_match.group(1)) < 7:
            if in_list:
                html += "</ul>"
                in_list = False
            level = len(header_match.group(1))
            content = _parse_emphasis(header_match.group(2))
            html += f"<h{level}>{content}</h{level}>"
        # List items
        elif line.startswith("* "):
            if not in_list:
                html += "<ul>"
                in_list = True
            content = _parse_emphasis(line[2:])
            html += f"<li>{content}</li>"
        # Paragraphs
        else:
            if in_list:
                html += "</ul>"
                in_list = False
            content = _parse_emphasis(line)
            html += f"<p>{content}</p>"

    if in_list:
        html += "</ul>"

    return html