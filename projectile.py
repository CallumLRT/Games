try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math


class Projectile:
    # img_url: url to image to display as enemy
    # dims: dimensions to draw on the canvas
    # pos: coordinates (as a tuple) to spawn the projectile at
    # speed: how fast the enemy moves
    # target: point which the fireball shoots to
    # frame_life: how many frames the projectile will last
    def __init__(self, img_url, dims, pos, speed, target, frame_life):
        self.IMG = simplegui.load_image(img_url)
        self.IMG_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.IMG_CENTRE = (self.IMG_DIMS[0] / 2, self.IMG_DIMS[1] / 2)
        self.DIMS = dims
        self.vel = target.copy().subtract(pos).normalize().multiply(speed)
        self.pos = pos.copy()
        self.speed = speed
        if self.vel.x == 0.0:
            if self.vel.y == 1*speed:
                self.imgRot = math.pi/2
            if self.vel.y == -1*speed:
                self.imgRot = -math.pi/2
        else:
            self.imgRot = math.atan(self.vel.y / self.vel.x)
        if self.vel.x < 0:
            self.imgRot = math.pi + self.imgRot
        self.frame_life = frame_life

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.DIMS, self.imgRot)

    def update(self):
        self.pos.add(self.vel)
        self.frame_life -= 1

    def collides(self, other):
        if self == other:
            return False
        else:
            dist = (self.pos - other.pos).length()
            collisionDist = (self.radius + self.border) + (other.radius + other.border)
            return dist <= collisionDist
