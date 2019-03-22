try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
import random
CANVAS_DIMS = globals.CANVAS_DIMS


class Room:
    def __init__(self):
        self.IMG = simplegui.load_image(
            'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Room.png?token=AexQrdRVNhD_QU5cQNkbuTH6MyOWBMkAks5clNUFwA%3D%3D')
        self.IMG_CENTRE = (300, 200)
        self.IMG_DIMS = (600, 400)
        self.IMG_Size = (600, 400)

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2),
                          (CANVAS_DIMS[0], CANVAS_DIMS[1]))
