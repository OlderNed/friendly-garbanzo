from Piece import Piece
from Tile import Tile


class Board:
    def __init__(self):
        """Creates a new Board object."""
        self.board = [[Tile() for i in range(8)] for i in range(8)]

    def print_board(self):
        """Prints the board"""
        for row in self.board: print(row)

   
    def __str__(self):
        return '\n'.join([str(l) for l in self.board])


    def place(self, color : str, x : int, y : int):
        new_piece = Piece(color)
        try:
            self.board[x][y].place(new_piece)
        except ValueError:
            print('Tile occupied')
            return False

        return True
        
    def check(self, x, y):
        horizontal_tiles = tiles = self.board[x]
        vertical_tiles = [self.board[i][y] for i in range(8)]
        print(vertical_tiles)
        # print(self.trim_edges(tiles))
            
    
    @staticmethod
    def trim_edges(row):
        """I don't know if this is needed."""
        while row[0].piece == Piece():
            row.pop(0)

        while row[-1].piece == Piece():
            row.pop(-1)

        return row


def test():
    board = Board()
    board.place('black', *(1,1))
    print(board)
    for i in range(2,5):
        board.place('white', *(1, i))
    # board.check(*(1,1))


test()
