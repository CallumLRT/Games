try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy
from fireball import Fireball
import math


# TODO make enemy stay at certain distance away from player
class RangedEnemy(Enemy):
    def __init__(self, pos):
        super().__init__("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/bluecircle.png",
                         (500, 500), (50, 50), pos, 2)

    def shoot(self, target):
        return Fireball(self.pos, target)

    def target(self, pos):
        super().target(pos.copy())
        if math.sqrt((self.pos.x - pos.x) ** 2 + (self.pos.y - pos.y) ** 2) < 200:
            self.vel = Vector(0, 0)
