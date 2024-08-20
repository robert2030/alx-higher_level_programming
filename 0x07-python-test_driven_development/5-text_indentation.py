#!/usr/bin/python3
"""
text with 2 new lines
"""


def text_indentation(text):
    """text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    if not text:
        return

    for char in text:
        if char in special_chars:
            lines.append(line.strip())
            lines.append('')
            line  = ''

    if line:
        lines.append(line.strip())

    forline in lines
    print (line)
