_ = False

game_map = [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,]
]

class Map:

    def __init__(self):

        self.game_map = game_map
        self.entity_pos = {}

    def get_entity_start_pos(self):

        for i, row in enumerate(self.game_map):
            for j, col in enumerate(row):
                if col:
                    self.entity_pos[i, j] = col

        return self.entity_pos
