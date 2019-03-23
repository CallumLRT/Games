try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy
from gates import Gate
import globals


# stores values for level
class Level5(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = [MeleeEnemy((globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 2))]
        self.RangedEnemies = []
        self.Rocks = []
        self.Gates = [Gate(3, 4, 2)]

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates, self.Rocks)
        Levels.printText = 5
