try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
import math


class Projectile:
    def __init__(self, img_url, img_dims, dims, pos, speed, target, frame_life):
        self.IMG = simplegui.load_image(img_url)
        self.IMG_DIMS = img_dims
        self.IMG_CENTRE = (img_dims[0] / 2, img_dims[1] / 2)
        self.DIMS = dims
        self.vel = target.copy().subtract(pos).normalize().multiply(speed)
        self.pos = pos.copy()
        self.speed = speed
        self.imgRot = math.atan(self.vel.y / self.vel.x)
        if self.vel.x < 0:
            self.imgRot = math.pi + self.imgRot
        self.frameLife = frame_life

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.DIMS, self.imgRot)

    def update(self):
        self.pos.add(self.vel)
        self.frameLife -= 1
