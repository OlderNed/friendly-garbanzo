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
        print('flip_row running')
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
            x, y = y, x
            # print('transposed board')
            # self.print_board()
        
        # print('pieces defined')
        pieces = list()
        # print('loop should start here')
        # print(f'x + x = {x + 1}\nend = {end}\ndirection_coefficient = {direction_coefficient}')
        # print(list(range(x+1, end, direction_coefficient)))
        # print(f'(x, y) : ({x}, {y})')

        for i in range(x + 1, end, direction_coefficient):
            print(i, y)
            c_piece = self.board[i][y]
            # print(c_piece)
            if str(c_piece) == '0':
                continue
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
    print('running flip_row')
    tiles = board.flip_rows(2, 0, 'p', 'y')
    print('flip_row done running')
    print(board)


test()
