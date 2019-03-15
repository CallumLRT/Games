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
from interactions import Interaction
from walls import Wall

# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

kbd = Keyboard()
wheel = Wheel()
playerInter = PlayerInteraction(wheel, kbd)

walls = []
walls.append(Wall(Vector(0, 0), Vector(CANVAS_DIMS[0], 0), Vector(0, 1)))
walls.append(Wall(Vector(CANVAS_DIMS[0], 0), Vector(CANVAS_DIMS[0], CANVAS_DIMS[1]), Vector(-1, 0)))
walls.append(Wall(Vector(0, CANVAS_DIMS[1]), Vector(CANVAS_DIMS[0], CANVAS_DIMS[1]), Vector(0, -1)))
walls.append(Wall(Vector(0, 0), Vector(0, CANVAS_DIMS[1]), Vector(1, 0)))

wall_interactions = []
for wall in walls:
    wall_interactions.append(Interaction(wheel, wall))


def draw(canvas):
    for wall in walls:
        wall.draw(canvas)
    for interaction in wall_interactions:
        interaction.update()
    playerInter.update()
    wheel.update()
    wheel.draw(canvas)


frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('white')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
