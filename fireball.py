try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from projectile import Projectile


class Fireball(Projectile):
    def __init__(self, origin, target):
        super().__init__(
            "https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/fireball-clipart-pixel-sprite-351661-3575577.png",
            (640, 480), (40, 30), origin, 3, target, 100)
