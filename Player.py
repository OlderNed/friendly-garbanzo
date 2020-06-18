from sys import argv

class Player:
    def __init__(self, color):
        """Creates a new `Player`object
        args:
                color -- The color of the piece the player should place """
        self.color = color

    def do_turn(self):
        """Returns a tuple (x,y) with coordinates where the piece should be placed"""
        # Lets take raw input for now.
        c = input('Place piece <x y>: ').split()
        c = (int(c[0]), int(c[1])) # TODO: Find a better way of doing this.
        return c


    def __repr__(self):
        return f"Player of color {self.color}"



def test():
    p = Player('White')
    p2 = Player('Black')
    print(p, p2)
    print(p.do_turn())


try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass

