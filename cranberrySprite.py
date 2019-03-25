try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy
import globals

class CranberrySprite:  # Unused class - was going to be used for health increase
    def __init__(self, pos):
        self.IMG = simplegui.load_image("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/SpriteCranberry.png")
        self.IMG_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.IMG_CENTRE = (self.IMG_DIMS[0] / 2, self.IMG_DIMS[1] / 2)
        self.DIMS = (50, 50)
        self.vel = Vector(0, 0)
        self.pos = Vector(pos[0], pos[1])
        self.speed = 1
        self.radius = 20
        self.border = -3
        self.pos = Vector(pos[0], pos[1])

    def collides(self, other):
        if self == other:
            return False
        else:
            dist = (self.pos - other.pos).length()
            collisionDist = (self.radius + self.border) + (other.radius + other.border)
            return dist <= collisionDist

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.DIMS)
