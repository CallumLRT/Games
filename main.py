try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
from vector import Vector
from interactions import Interaction
from walls import Wall
from levels import Levels
from level1 import Level1

# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

wall_interactions = []
for wall in Levels.Walls:
    wall_interactions.append(Interaction(Levels.player, wall))

level = Level1()


def draw(canvas):
    for interaction in wall_interactions:
        interaction.update()
    Levels.update()
    Levels.draw(canvas)


frame = simplegui.create_frame('Game', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('black')
frame.set_draw_handler(draw)
frame.set_keydown_handler(Levels.kbd.keyDown)
frame.set_keyup_handler(Levels.kbd.keyUp)
frame.start()
