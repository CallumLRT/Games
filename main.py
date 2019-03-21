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
from level2 import Level2
from level3 import Level3
from level4 import Level4
from level5 import Level5

# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

wall_interactions = []
for wall in Levels.Walls:
    wall_interactions.append(Interaction(Levels.player, wall))

level1 = Level1()
level1.LoadLevel()
level2 = Level2()
level3 = Level3()
level4 = Level4()
level5 = Level5()


def draw(canvas):
    # for interaction in wall_interactions:
    #     interaction.update()dwa
    Levels.update()
    Levels.draw(canvas)


frame = simplegui.create_frame('Game', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('black')
frame.set_draw_handler(draw)
frame.set_keydown_handler(Levels.kbd.keyDown)
frame.set_keyup_handler(Levels.kbd.keyUp)
frame.start()
