import pgzero
from entities import *

class Game:

    def __init__(self):

        self.block_list = []

        for i in range(10):
            self.block = Block()
            self.block_list.append(self.block)

    def draw_game(self):

        for block in self.block_list:
            block.draw_entity()

    def update_game(self):

        for block in self.block_list:
            block.update_entity()
