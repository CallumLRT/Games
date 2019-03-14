try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector


# Do not use directly, only inherit from
class Enemy:
    def __init__(self, img_url, img_dims, dims, pos, speed):
        self.IMG = simplegui.load_image(img_url)
        self.IMG_DIMS = img_dims
        self.IMG_CENTRE = (img_dims[0] / 2, img_dims[1] / 2)
        self.DIMS = dims
        self.vel = Vector(0, 0)
        self.pos = Vector(pos[0], pos[1])
        self.speed = speed

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.DIMS)

    def update(self):
        self.pos.add(self.vel.multiply(self.speed))
        self.vel.multiply(0.7)

    def target(self, pos):
        self.vel = Vector(pos.get_p()[0] - self.pos.get_p()[0], pos.get_p()[1] - self.pos.get_p()[1]).normalize()