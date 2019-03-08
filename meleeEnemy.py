try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from enemy import Enemy


class MeleeEnemy(Enemy):
    def __init__(self, pos):
        super().__init__("https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/fancycirlce.png",
                         (660, 660), (50, 50), pos, 2)
