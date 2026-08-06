import pgzero
from entities import *

class Game:

    def __init__(self):

        self.block_list = []

        for i in range(576):
            self.block = Block()
            self.block_list.append(self.block)

        self.player = Player()

    def draw_game(self):

        for block in self.block_list:
            block.draw_entity()

        self.player.draw_entity()

    def update_game(self):

        for block in self.block_list:
            block.update_entity()

        self.player.update_entity()
