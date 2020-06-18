from sys import argv

class Piece:
    # TODO
    # I'm not completely sold on doing it this way
    colors = {
            "white": "W",
            "black": "B",
            'null': '0'
            }

    def __init__(self, color : str):
        """Returns a new Piece object.
        args:
        color -- String representing color of the piece"""
        self.color = color.lower()

    def __repr__(self):
        return Piece.colors.get(self.color)


def test():
    wp = Piece('White')
    bp = Piece('Black')
    np = Piece('Null')
    print('White piece')
    print(wp)
    print('Black Piece')
    print(bp)
    print('Null piece')
    print(np)
try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass
