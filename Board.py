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
    def print_board(self):
        print(list(range(8)))
        for i, row in enumerate(self.board): print(row, [i])

    def flip_rows(self, x, y, direction='p', axis='x'):
        """Checks if any pieces can be flipped, and flips them"""
        
        piece = self.board[x][y]
        direction_coefficient = 0
        # apply direction for the loop
        if direction == 'p':
            direction_coefficient = 1
            end = 8
        else:
            direction_coefficient = -1
            end = 0
        # chose axis 
        if axis == 'y':
            self.transpose()
            self.print_board()
        

        pieces = list()
        for i in range(x + 1, end, direction_coefficient):
            c_piece = self.board[i][y]
            if str(c_piece) == '0':
                break
            else:
                pieces.append(((i, y)))
        last = pieces.pop(-1)
        if not (str(last) == '0' or str(last) == str(piece)):
            for piece in pieces:
                x,y = piece
                self.board[x][y].flip()
        
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
    board.place(black_pieces.pop(), 2,0)
    board.place(white_pieces.pop(), 2,1)
    board.place(white_pieces.pop(), 2,2)
    board.place(white_pieces.pop(), 2,3)
    board.place(black_pieces.pop(), 2,4)
    board.print_board()
    print('running check')
    tiles = board.flip_rows(2, 0, 'p', 'y')
    print('check done running')
    print(board)


test()
