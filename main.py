try:
    import simplegui
except ImportError:
    try:
        import simplegui2pygamemodule as simplegui
    except ImportError:
        try:
            import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
        except ImportError:
            print("rip")
            exit()

import pygame

import globals
from vector import Vector
from playerInteraction import PlayerInteraction
from keyboard import Keyboard
from wheel import Wheel
from drawWalls import DrawWalls
from interactions import Interactions
from walls import Walls



# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

kbd = Keyboard()
wheel = Wheel()
#walls = Walls()
playerInter = PlayerInteraction(wheel, kbd)
inter = Interactions(wheel)
drawWalls = DrawWalls()

def draw(canvas):
    #pygame.time.Clock().tick_busy_loop(60)
    playerInter.update()
    wheel.update()
    wheel.draw(canvas)
    DrawWalls.draw(canvas)
    inter.update()


frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('white')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
