try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector


# Do not use directly, only inherit from
class Enemy:
    def __init__(self, img, img_dims, dims, pos, speed):
        self.IMG = img
        self.IMG_DIMS = img_dims
        self.IMG_CENTRE = (img_dims[0] / 2, img_dims[1] / 2)
        self.DIMS = dims
        self.DIMS_CENTRE = (dims[0] / 2, dims[1] / 2)
        self.vel = Vector(0, 0)
        self.pos = pos
        self.speed = speed

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.DIMS_CENTRE, self.DIMS)

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.7)

    def target(self, pos):
        self.vel = pos.subtract(self.pos).normalize() * self.speed
