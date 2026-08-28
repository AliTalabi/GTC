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

                #pinkey

                if (
                        self.pinkey.entity.right == self.bluey.entity.left
                        and self.pinkey.entity.top < self.bluey.entity.bottom
                        and self.pinkey.entity.bottom > self.bluey.entity.top
                ):
                    self.pinkey.entity_blocked_directions.append('right')

                if (
                        self.pinkey.entity.left == self.bluey.entity.right
                        and self.pinkey.entity.top < self.bluey.entity.bottom
                        and self.pinkey.entity.bottom > self.bluey.entity.top
                ):
                    self.pinkey.entity_blocked_directions.append('left')

                if (
                        self.pinkey.entity.top == self.bluey.entity.bottom
                        and self.pinkey.entity.left < self.bluey.entity.right
                        and self.pinkey.entity.right > self.bluey.entity.left
                ):
                    self.pinkey.entity_blocked_directions.append('up')

                if (
                        self.pinkey.entity.bottom == self.bluey.entity.top
                        and self.pinkey.entity.left < self.bluey.entity.right
                        and self.pinkey.entity.right > self.bluey.entity.left
                ):
                    self.pinkey.entity_blocked_directions.append('down')

                #bluey

                if (
                        self.bluey.entity.right == self.pinkey.entity.left
                        and self.bluey.entity.top < self.pinkey.entity.bottom
                        and self.bluey.entity.bottom > self.pinkey.entity.top
                ):
                    self.bluey.entity_blocked_directions.append('right')

                if (
                        self.bluey.entity.left == self.pinkey.entity.right
                        and self.bluey.entity.top < self.pinkey.entity.bottom
                        and self.bluey.entity.bottom > self.pinkey.entity.top
                ):
                    self.bluey.entity_blocked_directions.append('left')

                if (
                        self.bluey.entity.top == self.pinkey.entity.bottom
                        and self.bluey.entity.left < self.pinkey.entity.right
                        and self.bluey.entity.right > self.pinkey.entity.left
                ):
                    self.bluey.entity_blocked_directions.append('up')

                if (
                        self.bluey.entity.bottom == self.pinkey.entity.top
                        and self.bluey.entity.left < self.pinkey.entity.right
                        and self.bluey.entity.right > self.pinkey.entity.left
                ):
                    self.bluey.entity_blocked_directions.append('down')
