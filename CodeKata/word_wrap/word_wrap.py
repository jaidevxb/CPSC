def word_wrap(text: str, column: int) -> str:
    """
    Wraps the text so that no line exceeds the given column width.
    Breaks only at spaces (word boundaries).
    """

    if not text:
        return ""

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        # If the current line is empty, just add the word
        if not current_line:
            current_line = word
        # If adding this word exceeds column limit, start new line
        elif len(current_line) + 1 + len(word) > column:
            lines.append(current_line)
            current_line = word
        else:
            current_line += " " + word

    if current_line:
        lines.append(current_line)

    return "\n".join(lines)
