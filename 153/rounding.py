from math import floor, ceil

def round_up_or_down(transactions, up=True):
    if up:
        return [ceil(number) for number in transactions]
    return [floor(number) for number in transactions]
