from pgzero.keyboard import keyboard

from map import *
from pgzero.actor import Actor
from game import *

entities_pos_dict = Map().get_entity_start_pos()

class Entity:

    def __init__(self, entity_image=None, entity_type=None):

        self.entity_image = entity_image
        self.entity = None
        self.entity_pos = ()
        self.entity_type = entity_type
        self.entity_define_bool = True
        self.entity_arrangement_bool = True

    def define_actor(self):

        if self.entity_define_bool:
            self.entity = Actor(self.entity_image, (10000, 10000))
            self.arrangement()
            self.entity_define_bool = False

        return self.entity

    def arrangement(self):

        if self.entity_arrangement_bool:

            for pos in entities_pos_dict:

                if entities_pos_dict[pos][0] == self.entity_type and entities_pos_dict[pos][1]:
                        for x_y in pos:
                            self.entity_pos += ((x_y * 40) + (40 / 2), )

                        self.entity_pos = self.entity_pos[::-1]
                        self.entity.pos = self.entity_pos

                        entities_pos_dict[pos] = (self.entity_type, False)

                        break

            self.entity_arrangement_bool = False

    def movement(self):
        pass

    def draw_entity(self):
        self.entity.draw()

    def update_entity(self):
        self.define_actor()
        self.movement()


class Block(Entity):
    def __init__(self, entity_image='block', entity_type=1):
        super().__init__(entity_image, entity_type)


class Player(Entity):

    def __init__(self, entity_image='player', entity_type=2):
        super().__init__(entity_image, entity_type)

    def movement(self):

        if keyboard.right and self.entity.x <= 1258:
            self.entity.x += 2

        if keyboard.left and self.entity.x >= 22:
            self.entity.x -= 2