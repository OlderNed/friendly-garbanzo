from Piece import Piece
from Tile import Tile


class Board:
    def __init__(self):
        """Creates a new Board object."""
        self.board = [[Tile() for i in range(8)] for i in range(8)]

    def print_board(self):
        """Prints the board"""
        for row in self.board: print(row)

    
    def place(self, color : str, x : int, y : int):
        try:
            self.board[x][y].place(Piece(color))
        except ValueError:
            print('Tile occupied')
            return False

        return True
        


def test():
    board = Board()
    print('basic board')
    board.print_board()
    print('adding black at 1,1')
    board.place('black', *(2,5))
    print()
    print('added black at 1,1')
    board.print_board()
    print('trying to place white at 1,1') 
    try:
        board.place('white', *(1,1))
    except ValueError as e:
        print('Exception caught:', e)
test()
