try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy
import globals

CANVAS_WIDTH = globals.CANVAS_DIMS[0]
CANVAS_HEIGHT = globals.CANVAS_DIMS[1]


class Rock(Enemy):
    def __init__(self, pos):
        super().__init__(
            "https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/rock.png?token=AexQrZ5LrNpxB4tlXs7pVENJNtB7v00yks5cnisHwA%3D%3D",
            (50, 50), pos, 1)
        self.radius = 25
        self.border = 1
        self.dazeCount = 0
        self.currentlyTargeting = True
        self.count = 0

    def dazed(self):
        self.dazeCount = 8  # Change for different 'Dazed' times (Larger Number = Longer)

    def daze_cycle(self):
        if self.dazeCount > 0:
            self.dazeCount -= 1
        else:
            self.currentlyTargeting = True

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
        self.currentlyTargeting = target  # Boolean for whether targetting is active

    def count_cycle(self):
        self.count -= 1

    def update(self):
        self.pos.add(self.vel)
        if self.outX():
            self.pos.x %= CANVAS_WIDTH
            if self.vel.x >= 0:
                self.pos.x -= self.radius
            else:
                self.pos.x += self.radius
        if self.outY():
            self.pos.y %= CANVAS_HEIGHT
            if self.vel.y >= 0:
                self.pos.y -= 2 * self.radius
            else:
                self.pos.y += 2 * self.radius

    def outX(self):
        return (self.pos.x + self.radius < 0 or
                self.pos.x - self.radius > CANVAS_WIDTH)

    def outY(self):
        return (self.pos.y + self.radius < 0 or
                self.pos.y - self.radius > CANVAS_HEIGHT)