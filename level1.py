try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from meleeEnemy import MeleeEnemy
from gates import Gate
import globals


class Level1(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = {MeleeEnemy((globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 4))}
        self.RangedEnemies = {}
        self.Gates = {Gate(0, 0, 1)}

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates)
        Levels.printText = 1
