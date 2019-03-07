from vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import pygame


class Wheel:
    def __init__(self):
        self.IMG = simplegui.load_image('images/wheel.png')
        self.IMG_CENTRE = (256, 256)
        self.IMG_DIMS = (512, 512)
        self.vel = Vector(3, 0)
        self.STEP = 0
        self.imgRadius = 64
        self.IMG_Size = (128, 128)
        self.pos = Vector(CANVAS_DIMS[0] / 2, 2 * CANVAS_DIMS[1] / 3.)
        self.imgRot = 0

    def draw(self, canvas):
        if (self.pos.x < -self.imgRadius):
            self.pos.x = CANVAS_DIMS[0] + self.imgRadius
        if (self.pos.x <= (CANVAS_DIMS[0] + self.imgRadius)):

            self.imgRot += self.STEP
            canvas.draw_image(self.IMG, (256, 256), (512, 512), self.pos.get_p(), self.IMG_Size, self.imgRot)
        else:
            self.pos.x = -self.imgRadius
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

WIDTH = 500
HEIGHT = 500
a = 0
b = 0


def randCol():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'


# Drawing handler:
# this function is called 60 times per second
def draw(canvas):
    global a
    global b
    if (a % 60 == 0):
        canvas.draw_circle((WIDTH / 2, HEIGHT / 2), 20, 40, 'green', 'white')
        canvas.draw_circle((240, 240), 20, 40, 'white', 'white')
        a = a + 1
    else:
        canvas.draw_circle((WIDTH / 2, HEIGHT / 2), 20, 40, 'red', 'white')
        canvas.draw_circle((240, 240), 20, 40, 'blue', 'white')
        a = a + 1
    b = b + 1


# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Colours", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
