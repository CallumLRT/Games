try:
    import simplegui
except ImportError:
    try:
        import simplegui2pygame as simplegui
    except ImportError:
        try:
            import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
        except ImportError:
            print("rip")
            exit()

import pygame

import globals
from vector import Vector
from interaction import Interaction
from keyboard import Keyboard
from wheel import Wheel

# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

kbd = Keyboard()
wheel = Wheel()
inter = Interaction(wheel, kbd)


def draw(canvas):
    pygame.time.Clock().tick_busy_loop(60)
    inter.update()
    wheel.update()
    wheel.draw(canvas)


frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('white')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
