WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    count = 1
    while count != size + 1:
        board = WHITE + BLACK
        if count % 2 == 0:
            board = BLACK + WHITE
        print(board * int(size / 2))
        count = count + 1
