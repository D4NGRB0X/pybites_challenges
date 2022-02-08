import re

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    _digits = re.compile(r'\d')
    filtered_names = [
        name
        for name in names
        if name[0] != IGNORE_CHAR and _digits.search(name) is None]
    new_names = []
    for name in filtered_names:
        if name[0] == QUIT_CHAR:
            break
        new_names.append(name)
    return new_names[0:MAX_NAMES]

