try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
import random

CANVAS_DIMS = globals.CANVAS_DIMS


class Room:
    def __init__(self):
        rr = random.randint(2, 3)
        # its broken
        # if (rr == 1):
        #     self.IMG = simplegui.load_image(
        #         'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Room.png?token=AexQrdRVNhD_QU5cQNkbuTH6MyOWBMkAks5clNUFwA%3D%3D')
        if (rr == 2):
            self.IMG = simplegui.load_image(
                'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Room5.png?token=AexQrXLZjEydOBja1Bl8qWzIoKTbItiwks5cngZFwA%3D%3D')
        if (rr == 3):
            self.IMG = simplegui.load_image(
                'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Room3.png?token=AexQrZwsvQ_8LIUX3H91nYznI9p5xjDNks5cngDmwA%3D%3D')
        # terrible background
        # if (rr == 4):
        #     self.IMG = simplegui.load_image(
        #         'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Room6.png?token=AexQrdaFTfNrqWUrjKaJdpd7lRzI8rjlks5cngZawA%3D%3D')

        self.IMG_CENTRE = (self.IMG.get_width() / 2, self.IMG.get_height() / 2)
        self.IMG_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.IMG_Size = (CANVAS_DIMS[0], CANVAS_DIMS[1])

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2),
                          (CANVAS_DIMS[0], CANVAS_DIMS[1]))
