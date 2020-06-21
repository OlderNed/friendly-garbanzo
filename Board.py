from Piece import Piece


class Board:
    def __init__(self):
        """Creates a new Board object."""
        self.board = [[Piece() for i in range(8)] for i in range(8)]
    
   
    def __str__(self):
        return '\n'.join([str(l) for l in self.board])

    
    def place(self, piece, x, y, alt=False):
        """Places a tile on the given coordinates"""
        self.board[x][y] = piece


def test():
    board = Board()
    black_pieces = [Piece('black') for _ in range(8)]
    white_pieces = [Piece('white') for _ in range(8)]
    board.place(black_pieces.pop(), 2,2)
    board.place(white_pieces.pop(), 3,2)
    board.place(white_pieces.pop(), 4,2)
    board.place(white_pieces.pop(), 5,2)
    board.place(black_pieces.pop(), 6,2)
    print(board)

test()
