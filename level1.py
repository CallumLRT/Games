try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy
from gates import Gate


class Level1(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = {MeleeEnemy((500, 100))}
        self.RangedEnemies = {}
        self.Gates = {Gate(0, 0, 1)}

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates)
