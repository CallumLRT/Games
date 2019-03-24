try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
import random

CANVAS_DIMS = globals.CANVAS_DIMS


class Menu:
    def __init__(self):
        self.game_start = False

        self.IMG = simplegui.load_image(
            'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Simple_grey.png?token=AexQrWRp93DDGdtspxKgQRIo_NppOK6Gks5coMbQwA%3D%3D')
        self.IMG_CENTRE = (self.IMG.get_width() / 2, self.IMG.get_height() / 2)
        self.IMG_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.IMG_Size = (CANVAS_DIMS[0], CANVAS_DIMS[1])
        self.IMG_Pos = (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2)  # where to draw image

        self.BUTT = simplegui.load_image(
            'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Start_button.png?token=AexQrbMnYHDhtdp3TYrgjTkO46pzViXQks5coMtLwA%3D%3D')
        self.BUTT_CENTRE = (self.BUTT.get_width() / 2, self.BUTT.get_height() / 2)
        self.BUTT_DIMS = (self.BUTT.get_width(), self.BUTT.get_height())
        self.BUTT_Size = self.BUTT_DIMS
        self.BUTT_Pos = (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2)  # where to draw image

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.IMG_Pos,
                          self.IMG_Size)
        canvas.draw_image(self.BUTT, self.BUTT_CENTRE, self.BUTT_DIMS, self.BUTT_Pos,
                          self.BUTT_Size)
