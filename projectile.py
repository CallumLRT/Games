try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math


class Projectile:
    def __init__(self, img_url, dims, pos, speed, target, frame_life):
        self.IMG = simplegui.load_image(img_url)
        self.IMG_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.IMG_CENTRE = (self.IMG_DIMS[0] / 2, self.IMG_DIMS[1] / 2)
        self.DIMS = dims
        self.vel = target.copy().subtract(pos).normalize().multiply(speed)
        self.pos = pos.copy()
        self.speed = speed
        self.imgRot = math.atan(self.vel.y / self.vel.x)
        if self.vel.x < 0:
            self.imgRot = math.pi + self.imgRot
        self.frame_life = frame_life

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.DIMS, self.imgRot)

    def update(self):
        self.pos.add(self.vel)
        self.frame_life -= 1
