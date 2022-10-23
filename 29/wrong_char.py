def get_index_different_char(chars):
    alpha_num_char, not_alpha_num_char = [], []
    for char in chars:
        if str(char).isalnum():
            alpha_num_char.append(char)
        else:
            not_alpha_num_char.append(char)
    if len(alpha_num_char) < len(not_alpha_num_char):
        return chars.index(alpha_num_char[0])
    return chars.index(not_alpha_num_char[0])
