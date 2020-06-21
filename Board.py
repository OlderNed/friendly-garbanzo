from Piece import Piece


class Board:
    def __init__(self):
        """Creates a new Board object."""
        self.board = [[Piece() for i in range(8)] for i in range(8)]
        self.transposed = False
    
   
    def __str__(self):
        return '\n'.join([str(l) for l in self.board])

    
    def place(self, piece, x, y, alt=False):
        """Places a tile on the given coordinates"""
        self.board[x][y] = piece
    

    def check(self, x, y, direction='p', axis='x'):
        piece = self.board[x][y]
        direction_coefficient = 0
        if direction == 'p':
            direction_coefficient = 1
            end = 8
        else:
            direction_coefficient = -1
            end = 0

        if axis == 'y':
            self.transpose()

        # positive x direction
        pieces = list()
        for i in range(x + 1, end, direction_coefficient):
            c_piece = self.board[i][y]
            if str(c_piece) == '0':
                break
            else:
                pieces.append(((i, y)))
        
        pieces.pop(-1)
        for piece in pieces:
            x,y = piece
            self.board[x][y].flip()
            # piece = [C, (x, y)], where C is the color of the piece.
        
        if self.transposed:
            self.transpose()
        return pieces

    def transpose(self):
        self.board = [[row[i] for row in self.board] for i in range(8)]
        self.transposed = True


def test():
    board = Board()
    black_pieces = [Piece('black') for _ in range(8)]
    white_pieces = [Piece('white') for _ in range(8)]
    board.place(black_pieces.pop(), 2,2)
    board.place(white_pieces.pop(), 2,3)
    board.place(white_pieces.pop(), 2,4)
    board.place(white_pieces.pop(), 2,5)
    board.place(black_pieces.pop(), 2,6)
    print(board)
    print('running check')
    tiles = board.check(2,2, 'p', 'y')
    print('check done running')
    print(board)


test()
