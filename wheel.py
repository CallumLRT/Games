try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
import globals

CANVAS_DIMS = globals.CANVAS_DIMS


class Wheel:
    def __init__(self):
        self.IMG = simplegui.load_image('https://img.itch.zone/aW1hZ2UvNzQ5MjIvMzQ3MTI2LmpwZw==/original/fcga2A.jpg')
        self.IMG_CENTRE = (256, 256)
        self.IMG_DIMS = (512, 512)
        self.vel = Vector(3, 0)
        self.STEP = 0
        self.imgRadius = 64
        self.IMG_Size = (128, 128)
        self.pos = Vector(CANVAS_DIMS[0] / 2, 2 * CANVAS_DIMS[1] / 3.)
        self.imgRot = 0
        self.radius = 20

    def draw(self, canvas):
        if self.pos.x < -self.imgRadius:
            self.pos.x = CANVAS_DIMS[0] + self.imgRadius
        if self.pos.x <= (CANVAS_DIMS[0] + self.imgRadius):

            self.imgRot += self.STEP
            canvas.draw_circle(self.pos.get_p(), 20, 12, 'green')
            # canvas.draw_image(self.IMG, (256, 256), (512, 512), self.pos.get_p(), self.IMG_Size, self.imgRot)
        else:
            self.pos.x = -self.imgRadius

    def bounce(self, normal):
        self.vel.reflect(normal)

    def update(self):
        self.pos.add(self.vel)
        self.wrap()
        self.vel.multiply(0.9)
        if self.vel.x < -0.005:
            self.STEP = 0.5
        elif self.vel.x > 0.005:
            self.STEP = -0.5
        else:
            self.STEP = 0

    def wrap(self):
        self.pos.x %= CANVAS_DIMS[0]
        self.pos.y %= CANVAS_DIMS[1]
