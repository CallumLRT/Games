try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy
from fireball import Fireball
from health import Health
import math
from random import randint

#https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/SpriteCran.png

class RangedEnemy(Enemy):
    # pos: coordinates to spawn at
    def __init__(self, pos):
        super().__init__("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/bluecircle.png",
                         (50, 50), pos, 1)
        self.cooldown = randint(100, 140)
        self.cooldown_max = self.cooldown
        self.radius = 25
        self.border = 1
        self.dazeCount = 0
        self.health = Health()

    def dazed(self):
        self.dazeCount = 5  # Change for different 'Dazed' times (Larger Number = Longer)

    # target: coordinates to shoot at
    def shoot(self, target):
        self.cooldown = self.cooldown_max
        return Fireball(self.pos, target)

    def set_target(self, target):
        self.currentlyTargeting = target


    def target(self, pos):
        if math.sqrt((self.pos.x - pos.x) ** 2 + (self.pos.y - pos.y) ** 2) < 200:
            self.vel = Vector(0, 0)
        elif self.currentlyTargeting and self.dazeCount == 0:
            super().target(pos.copy())
        else:
            self.daze_cycle()
    '''
    # pos: coordinates of target (player?)
    def target(self, pos):
        if math.sqrt((self.pos.x - pos.x) ** 2 + (self.pos.y - pos.y) ** 2) < 200:
            self.vel = Vector(0, 0)
        else:
            super().target(pos.copy())'''

    def update(self):
        super().update()
        self.cooldown -= 1

    def bounce(self, normal):
        self.vel.reflect(normal)

    def collides(self, other):
        if self == other:
            return False
        else:
            dist = (self.pos - other.pos).length()
            collisionDist = (self.radius + self.border) + (other.radius + other.border)
            return dist <= collisionDist
