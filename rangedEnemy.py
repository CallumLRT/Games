try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy
from fireball import Fireball
import math
from random import randint


class RangedEnemy(Enemy):
    def __init__(self, pos):
        super().__init__("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/bluecircle.png",
                         (500, 500), (50, 50), pos, 2)
        self.cooldown = randint(100, 140)
        self.cooldown_max = self.cooldown

    def shoot(self, target):
        self.cooldown = self.cooldown_max
        return Fireball(self.pos, target)

    def target(self, pos):
        if math.sqrt((self.pos.x - pos.x) ** 2 + (self.pos.y - pos.y) ** 2) < 200:
            self.vel = Vector(0, 0)
        else:
            super().target(pos.copy())

    def update(self):
        super().update()
        self.cooldown -= 1
