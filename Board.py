from sys import argv
from Piece import Piece
from Tile import Tile


class Board:
    def __init__(self):
        """Creates a new Board object."""
        self.board = [[Tile(Piece('null'))]*8]*8


    def print_board(self):
        """Prints the board"""
        for row in self.board: print(row)

    
    def place(self, color : str, x : int, y : int):
        try:
            self.board[x][y].place(Piece(color))
        except ValueError:
            print('Tile occupied')
            return False
        


def test():
    board = Board()
    board.print_board()

try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass

