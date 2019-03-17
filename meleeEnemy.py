try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy


class MeleeEnemy(Enemy):
    def __init__(self, pos):
        super().__init__("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/fancycircle.png",
                         (660, 660), (50, 50), pos, 1)
        self.radius = 25
        self.border = 1
        self.currentlyNotTarget = False
        self.dazeCount = 0

    def dazed(self):
        self.dazeCount = 60

    def daze_cycle(self):
        if self.dazeCount > 0:
            self.dazeCount -= 1
        else:
            self.currentlyNotTarget = False

    def collides(self, other):
        if self == other:
            return False
        else:
            dist = (self.pos - other.pos).length()
            collisionDist = (self.radius + self.border) + (other.radius + other.border)
            return dist <= collisionDist

    def bounce(self, normal):
        self.vel.reflect(normal)