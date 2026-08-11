from pgzero.keyboard import keyboard

from map import *
from pgzero.actor import Actor

from settings import GRAVITY

entities_pos_dict = Map().get_entity_start_pos()

class Entity:

    def __init__(self, entity_image=None, entity_type=None):

        self.entity_image = entity_image
        self.entity = None
        self.entity_pos = ()
        self.entity_type = entity_type
        self.entity_define_bool = True
        self.entity_arrangement_bool = True
        self.gravity = GRAVITY

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
        self.entity_blocked_directions = ['down']
        self.jump_power = -10
        self.gravity = GRAVITY
        self.y_speed = 0

    def movement(self):

        self.y_speed += self.gravity

        if keyboard.right and self.entity.x < 1260 and 'right' not in self.entity_blocked_directions:
            self.entity.x += 3.5

        if keyboard.left and self.entity.x > 20 and 'left' not in self.entity_blocked_directions:
            self.entity.x -= 3.5

        if (keyboard.space and self.entity.y > 20 and 'up' not in self.entity_blocked_directions and
                'down' in self.entity_blocked_directions):

            self.y_speed = self.jump_power
            self.entity_blocked_directions.remove('down')

        if 'down' not in self.entity_blocked_directions and 'up' not in self.entity_blocked_directions and self.entity.y < 700:
            self.entity.y += self.y_speed

        if 'down' in self.entity_blocked_directions:
            self.y_speed = 5
