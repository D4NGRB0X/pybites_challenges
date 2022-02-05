from statistics import mode


def freq_digit(num: int) -> int:
    numlist = list(map(int, str(num)))
    return mode(numlist)
