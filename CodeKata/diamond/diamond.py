def diamond(letter: str) -> str:
    """
    Return the diamond as a single string (lines joined with '\n') for the given uppercase letter.
    Assumes `letter` is a single uppercase letter 'A'..'Z'.
    """
    if not letter or len(letter) != 1 or not letter.isalpha():
        raise ValueError("Provide a single letter A-Z")

    letter = letter.upper()
    n = ord(letter) - ord('A')

    lines = []
    for i in range(0, n + 1):
        ch = chr(ord('A') + i)
        left = ' ' * (n - i)
        if i == 0:
            line = f"{left}{ch}"
        else:
            inner = ' ' * (2 * i - 1)
            line = f"{left}{ch}{inner}{ch}"
        lines.append(line)

    # mirror (exclude middle)
    bottom = list(reversed(lines[:-1]))
    all_lines = lines + bottom
    return "\n".join(all_lines)

def print_diamond(letter: str) -> None:
    """Prints the diamond to stdout (helper for manual run)."""
    print(diamond(letter))
