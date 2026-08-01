from map import *
from pgzero.actor import Actor
from game import *

class Entity:

    def __init__(self, entity_image=None, entity_type=None):

        self.entity_image = entity_image
        self.entity = None
        self.entity_pos = None
        self.entities_pos_dict = None
        self.entity_type = entity_type
        self.entity_define_bool = True
        self.entity_arrangement_bool = True

    def define_actor(self):

        if self.entity_define_bool:

            self.entity = Actor(self.entity_image)
            self.entity_define_bool = False

        return self.entity

    def arrangement(self):

        if self.entity_arrangement_bool:

            self.entities_pos_dict = Map().get_entity_start_pos()

            for pos in self.entities_pos_dict:
                if self.entity_pos[pos] == self.entity_type:
                    for x_y in pos:
                        self.entity_pos += ((x_y + 1) * 80 + (80 / 2), )

                    self.entity_pos = self.entity_pos[::-1]

                    self.name.pos = self.entity_pos

            self.entity_arrangement_bool = False


    def draw_entity(self):
        self.entity.draw()

    def update_entity(self):
        self.define_actor()
        self.arrangement()


class Block(Entity):
    def __init__(self, entity_image='block', entity_type='block'):
        super().__init__(entity_image, entity_type)
