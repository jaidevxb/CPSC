import re

def filename_range(filename: str) -> tuple[int, int]:
    # 1. Split directory and file name
    if "/" in filename:
        dir_part, name = filename.rsplit("/", 1)
        dir_len = len(dir_part) + 1  # +1 for slash
    else:
        name = filename
        dir_len = 0

    # 2. Remove extension
    name_wo_ext = re.sub(r"\.[^.]+$", "", name)

    # 3. Find the "core" name — the part *after* test/spec/steps/tests
    match = re.search(r"(?:test[_\-.]?|spec[_\-.]?|steps[_\-.]?|tests[_\-.]?)([A-Za-z0-9]+)", name_wo_ext, re.IGNORECASE)
    if match:
        start = match.start(1)  # start of group 1 (the core name)
        end = match.end(1)
        return (dir_len + start, dir_len + end)

    # 4. If pattern not found, try finding the last "/" and return the core part
    match2 = re.search(r"([A-Za-z0-9]+)(?:[_\-.]?(test|spec|steps|tests))?$", name_wo_ext, re.IGNORECASE)
    if match2:
        start = match2.start(1)
        end = match2.end(1)
        return (dir_len + start, dir_len + end)

    # 5. Fallback: everything before extension
    return (dir_len, dir_len + len(name_wo_ext))
