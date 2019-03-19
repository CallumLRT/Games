try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy


class Level1(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies.append(MeleeEnemy((500, 100)))
        self.MeleeEnemies.append(MeleeEnemy((100, 100)))
        self.RangedEnemies.append(RangedEnemy((100, 100)))
