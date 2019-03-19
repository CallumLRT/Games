try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy
from gates import Gate
import globals


class Level2(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = {MeleeEnemy((globals.CANVAS_DIMS[0] / 3, globals.CANVAS_DIMS[1] / 2)),
                             MeleeEnemy(((globals.CANVAS_DIMS[0] / 3 * 2), globals.CANVAS_DIMS[1] / 2))}
        self.RangedEnemies = {RangedEnemy((globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 2))}
        self.Gates = {Gate(2, 1, 0), Gate(1, 1, 2)}

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates)
        Levels.printText = 2
