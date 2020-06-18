from sys import argv
from Piece import Piece

class Tile:
    def __init__(self, piece=None):
        """Creates a new Tile object."""
        self.piece = piece

    def __repr__(self):
        if self.piece:
            return Piece.colors.get(self.piece.color)
        return '0'

    def place(self, piece):
        """Places a piece onto the tile."""
        if self.piece:
            raise ValueError("Can not place on an occupied tile.")
        else:
            self.piece = piece

    def change_color(self):
        """Changes the color of the tile."""
        if self.piece:
            if self.piece.color == 'black':
                self.piece = Piece('White')
            else:
                self.piece = Piece('Black')
        else:
            raise ValueError('Tile is empty.')
# Testing
def test():
    print('Test start')
    wp = Piece('White')
    bp = Piece('Black')
    et = Tile()
    wt = Tile(wp)
    bt = Tile(bp)
    print('white piece')
    print(wp)
    print('black piece')
    print(bp)
    print('empty tile')
    print(et)
    print('tile with white piece')
    print(wt)
    print('tile with black piece')
    print(bt)
    print('Changing color of black piece on tile bt')
    bt.change_color()
    print('color changed')
    print(bt)
    print('Test end')


try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass
