from sys import argv

class Piece:
    # TODO
    # I'm not completely sold on doing it this way
    colors = {
            "white": "W",
            "black": "B",
            'null': '0'
            }
    flip_dict = {
                'white': 'black',
                'black': 'white'
            }

    def __init__(self, color='null'):
        """Returns a new Piece object.
        args:
        color -- String representing color of the piece"""
        self.color = color.lower()

    def __repr__(self):
        return Piece.colors.get(self.color)
    
    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return self.color == other.color
    
    def flip(self):
        if str(self) == '0':
            raise ValueError('Can not flip a null piece!')
        self.color = Piece.flip_dict.get(self.color)

def test():
    wp = Piece('White')
    bp = Piece('Black')
    np = Piece('Null')
    print('White piece')
    print(wp)
    print('Black Piece')
    print(bp)
    print('flipping black piece')
    bp.flip()
    print('black piece flipped, bp is now', bp)
    print('Null piece')
    print(np)

if __name__ == '__main__':
    test()
