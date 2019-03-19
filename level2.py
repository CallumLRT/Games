try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy
from gates import Gate


class Level2(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = {MeleeEnemy((500, 100)), MeleeEnemy((100, 100))}
        self.RangedEnemies = {RangedEnemy((100, 100))}
        self.Gates = {Gate(2, 1, 0)}

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates)
