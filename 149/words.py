def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    srt = sorted(words, key=str.lower)
    digit = [word for word in srt if word[0].isdigit()]
    srt = srt[len(digit):]
    return srt+digit