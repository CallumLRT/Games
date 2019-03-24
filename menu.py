try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
import random
CANVAS_DIMS = globals.CANVAS_DIMS

class Menu:
    def __init__(self):
        self.IMG = simplegui.load_image('https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Simple_grey.png?token=AexQrWRp93DDGdtspxKgQRIo_NppOK6Gks5coMbQwA%3D%3D')
        self.IMG_CENTRE = (300, 200)
        self.IMG_DIMS = (600, 400)
        self.IMG_Size = (600, 400)

        self.BUTT = simplegui.load_image('https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Start_button.png?token=AexQrbMnYHDhtdp3TYrgjTkO46pzViXQks5coMtLwA%3D%3D')
        self.BUTT_CENTRE = (500, 300)
        self.BUTT_DIMS = (1000, 600)
        self.BUTT_Size = (1000,600)

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2),
                          (CANVAS_DIMS[0], CANVAS_DIMS[1]))
        canvas.draw_image(self.BUTT, self.BUTT_CENTRE, self.BUTT_DIMS, (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2),
                          (CANVAS_DIMS[0], CANVAS_DIMS[1]))