import re

def filename_range(filename: str) -> tuple[int, int]:
    """
    Calculates the start and end indices for the selected part of a filename 
    based on the specified renaming conventions.

    The selection excludes:
    1. The directory path (everything before the last '/').
    2. The file extension (everything after the last '.').
    3. Leading or trailing test/spec/step keywords, along with surrounding 
       separator characters (._-).
    
    Args:
        filename: The full filename string, including path and extension.

    Returns:
        A tuple (start_index, end_index) representing the selected range.
    """
    
    # 1. Find the absolute start index (excluding path)
    path_sep_index = filename.rfind('/')
    base_start = path_sep_index + 1

    # 2. Find the absolute end index (excluding extension)
    extension_sep_index = filename.rfind('.')
    
    # If the last dot is before or at the path start, or no dot exists, include everything after path
    if extension_sep_index <= path_sep_index:
        base_end = len(filename)
    else:
        base_end = extension_sep_index

    # The string we analyze (between path and extension)
    search_string = filename[base_start:base_end]
    select_start = 0
    select_end = len(search_string)

    # Keywords, ordered by length descending to ensure longest matches first (e.g., 'tests' before 'test')
    keywords = ('steps', 'tests', 'spec', 'step', 'test')
    # Separator characters are dot (.), underscore (_), and hyphen (-)
    separators = '[._-]'
    
    # --- A. Leading Pattern Exclusion (updates select_start) ---
    # Pattern: Must be at the start: ^(keyword)(separator)?
    leading_pattern = re.compile(f"^({'|'.join(keywords)})({separators})?", re.IGNORECASE)
    match = leading_pattern.match(search_string)
    
    if match:
        # Skip the entire matched pattern (keyword + optional separator)
        select_start = match.end()

    # --- B. Trailing Pattern Exclusion (updates select_end) ---
    # Pattern: (separator)?(keyword)$
    
    # Only search the string *after* the leading skip
    search_for_trailing = search_string[select_start:]
    
    if search_for_trailing:
        trailing_pattern = re.compile(f"({separators})?({'|'.join(keywords)})$", re.IGNORECASE)
        # We use search() with the $ anchor to ensure it's at the end of the substring
        match = trailing_pattern.search(search_for_trailing)
        
        if match:
            # The match.start() is relative to search_for_trailing. 
            # This is the index (relative to search_string) where the keyword-and-sep begins.
            new_select_end_relative = select_start + match.start()
            
            # The new end must be after the start of the selection to be valid
            if new_select_end_relative > select_start:
                 select_end = new_select_end_relative

    # 4. Convert relative selection indices to absolute indices in the original filename
    final_start = base_start + select_start
    final_end = base_start + select_end
    
    # Ensure start is not greater than end (e.g., for file named just 'test')
    if final_start > final_end:
        final_end = final_start

    return (final_start, final_end)
