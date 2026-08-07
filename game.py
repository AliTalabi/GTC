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
        self.player.entity_blocked_directions = []

        for block in self.block_list:

            if (
                    self.player.entity.right == block.entity.left
                    and self.player.entity.top < block.entity.bottom
                    and self.player.entity.bottom > block.entity.top
            ):
                self.player.entity_blocked_directions.append('right')

            if (
                    self.player.entity.left == block.entity.right
                    and self.player.entity.top < block.entity.bottom
                    and self.player.entity.bottom > block.entity.top
            ):
                self.player.entity_blocked_directions.append('left')

            if (
                    self.player.entity.top == block.entity.bottom
                    and self.player.entity.left < block.entity.right
                    and self.player.entity.right > block.entity.left
            ):
                self.player.entity_blocked_directions.append('up')

            if (
                    self.player.entity.bottom == block.entity.top
                    and self.player.entity.left < block.entity.right
                    and self.player.entity.right > block.entity.left
            ):
                self.player.entity_blocked_directions.append('down')