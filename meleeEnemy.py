try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy
from time import *


class MeleeEnemy(Enemy):
    def __init__(self, pos):
        super().__init__("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/fancycircle.png",
                         (660, 660), (50, 50), pos, 1)
        self.radius = 25
        self.border = 1
        self.currentlyNotTarget = False
        self.dazeCount = 0
        self.currentlyTargeting = True
        self.count = 0

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

    def set_target(self, target):
        self.currentlyTargeting = target #Boolean for whether targetting is active
        if target:
            print("true")
        else:
            self.bounce(self.pos)
            self.count = 100
            print("false")

    def count_cycle(self):
        self.count -= 1

    def target(self, pos):
        if self.currentlyTargeting and self.count == 0:
            self.vel = Vector(pos.get_p()[0] - self.pos.get_p()[0], pos.get_p()[1] - self.pos.get_p()[1]).normalize()
        else:
            self.count_cycle()
