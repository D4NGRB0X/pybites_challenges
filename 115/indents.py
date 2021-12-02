def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    count = len(text)-len(text.lstrip(" "))
    return count