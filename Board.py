from sys import argv
from Piece import Piece


class Board:
    def __init__(self):
        """Creates a new Board object."""
        self.board = [[Piece('Null')]*8]*8


    def print_board(self):
        """Prints the board"""
        for row in self.board: print(row)

    
    def place(self, color : str, coordinates : tuple):
        pass        

def test():
    board = Board()
    board.print_board()

try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass

