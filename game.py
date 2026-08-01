from entities import *

class Game:

    def __init__(self):

        self.block = Block()

    def draw_game(self):

        self.block.draw_entity()

    def update_game(self):

        self.block.update_entity()