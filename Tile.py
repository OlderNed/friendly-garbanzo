from Piece import Piece

class Tile:
    def __init__(self, piece=Piece('Null')):
        """Creates a new Tile object."""
        if not type(piece) == Piece:
            raise ValueError(f'Expected Piece.Pice tbut got {type(piece)}')
        self.piece = piece

    def __repr__(self):
        if self.piece:
            return Piece.colors.get(self.piece.color)
        return '0'

    def place(self, piece):
        """Places a piece onto the tile."""
        if self.piece.color != 'null':
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
    print('empty tile')
    print(et)
    print('placing white piece on empty tile')
    et.place(wp)
    print('white piece placed')
    print(et)
    print('placing black piece on et (expecting error)')
    try:
        bt.place(bp)
    except ValueError as e:
        print('Exception caught:', e)
    print('Test end')


