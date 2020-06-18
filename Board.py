from sys import argv

class Board:
    def __init__(self,):
        self.board = [[0]*8]*8


    def print_board(self):
        for row in self.board: print(row)


def test():
    board = Board()
    board.print_board()

try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass

