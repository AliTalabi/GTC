import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

import pgzrun
from settings import *
from game import *

game = Game()

def draw():
    screen.clear()
    game.draw_game()

def update():
    game.update_game()

pgzrun.go()
