try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy
from projectile import Projectile


class RangedEnemy(Enemy):
    def __init__(self, pos):
        super().__init__("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/bluecircle.png",
                         (500, 500), (50, 50), pos, 2)

    def shoot(self, target):
        return Projectile(self.pos.get_p(), target)
