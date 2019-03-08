try:
    import simplegui
except ImportError:
    try:
        import simplegui2pygamemodule as simplegui
    except ImportError:
        try:
            import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
        except ImportError:
            print("R.I.P")
            exit()

from vector import Vector
import globals

CANVAS_DIMS = globals.CANVAS_DIMS


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
        if self.pos.x < -self.imgRadius:
            self.pos.x = CANVAS_DIMS[0] + self.imgRadius
        if self.pos.x <= (CANVAS_DIMS[0] + self.imgRadius):

            self.imgRot += self.STEP
            canvas.draw_circle(self.pos.get_p(), 20, 12, 'Green')
            #canvas.draw_image(self.IMG, (256, 256), (512, 512), self.pos.get_p(), self.IMG_Size, self.imgRot)
        else:
            self.pos.x = -self.imgRadius

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.9)
        if self.vel.x < -0.005:
            self.STEP = 0.5
        elif self.vel.x > 0.005:
            self.STEP = -0.5
        else:
            self.STEP = 0
