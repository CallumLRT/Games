try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector


# Do not use directly, only inherit from
class Enemy:
    # img_url: url to image to display as enemy
    # dims: dimensions to draw on the canvas
    # pos: coordinates (as a tuple) to spawn the enemy at
    # speed: how fast the enemy moves
    def __init__(self, img_url, dims, pos, speed):
        self.IMG = simplegui.load_image(img_url)
        self.IMG_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.IMG_CENTRE = (self.IMG_DIMS[0] / 2, self.IMG_DIMS[1] / 2)
        self.DIMS = dims
        self.vel = Vector(0, 0)
        self.pos = Vector(pos[0], pos[1])
        self.speed = speed
        self.currentlyTargeting = True

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.DIMS)

    def update(self):
        self.pos.add(self.vel.multiply(self.speed))
        self.vel.multiply(0.7)

    def target(self, pos):
        self.vel = Vector(pos.get_p()[0] - self.pos.get_p()[0], pos.get_p()[1] - self.pos.get_p()[1]).normalize()

    def daze_cycle(self):
        if self.dazeCount > 0:
            self.dazeCount -= 1
        else:
            self.currentlyTargeting = True
