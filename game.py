import pgzero
from entities import *

class Game:

    def __init__(self):

        self.block_list = []

        for i in range(576):
            self.block = Block()
            self.block_list.append(self.block)

        self.pinkey = Pinkey()
        self.bluey = Bluey()

        self.players_list = [self.pinkey, self.bluey]

    def draw_game(self):

        for block in self.block_list:
            block.draw_entity()

        self.pinkey.draw_entity()
        self.bluey.draw_entity()

    def update_game(self):

        for block in self.block_list:
            block.update_entity()

        self.pinkey.update_entity()
        self.bluey.update_entity()

        for player in self.players_list:
            player.entity_blocked_directions = []

            for block in self.block_list:

                if (
                        player.entity.right == block.entity.left
                        and player.entity.top < block.entity.bottom
                        and player.entity.bottom > block.entity.top
                ):
                    player.entity_blocked_directions.append('right')

                if (
                        player.entity.left == block.entity.right
                        and player.entity.top < block.entity.bottom
                        and player.entity.bottom > block.entity.top
                ):
                    player.entity_blocked_directions.append('left')

                if (
                        player.entity.top == block.entity.bottom
                        and player.entity.left < block.entity.right
                        and player.entity.right > block.entity.left
                ):
                    player.entity_blocked_directions.append('up')

                if (
                        player.entity.bottom == block.entity.top
                        and player.entity.left < block.entity.right
                        and player.entity.right > block.entity.left
                ):
                    player.entity_blocked_directions.append('down')
