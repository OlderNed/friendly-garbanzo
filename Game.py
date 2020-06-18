from sys import argv
from Board import Board
from Player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []


def test():
    pass

try:
    if argv[1] == 'test':
        test()
except IndexError:
    pass

