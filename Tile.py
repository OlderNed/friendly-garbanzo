from sys import argv
from Piece import Piece

class Tile:
    def __init__(self, piece=None):
        self.piece = piece

    def __repr__(self):
        if self.piece:
            return Piece.colors.get(self.piece.color)
        return '0'

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
    print('Test end')


try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass
