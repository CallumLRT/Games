try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from rock import Rock
from meleeEnemy import MeleeEnemy
from superMeleeEnemy import SuperMeleeEnemy
from rangedEnemy import RangedEnemy
from gates import Gate
from room import Room
import globals


# stores values for level
class Level3(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = [MeleeEnemy(((globals.CANVAS_DIMS[0] / 9) * 2, (globals.CANVAS_DIMS[1] / 9) * 3)),
                             MeleeEnemy(((globals.CANVAS_DIMS[0] / 9) * 6, (globals.CANVAS_DIMS[1] / 9) * 4)),
                             MeleeEnemy(((globals.CANVAS_DIMS[0] / 9) * 5, (globals.CANVAS_DIMS[1] / 9) * 7)),
                             SuperMeleeEnemy(((globals.CANVAS_DIMS[0] / 9) * 8, (globals.CANVAS_DIMS[1] / 9) * 1))]
        self.RangedEnemies = [RangedEnemy(((globals.CANVAS_DIMS[0] / 9) * 2, (globals.CANVAS_DIMS[1] / 9) * 8)),
                              RangedEnemy(((globals.CANVAS_DIMS[0] / 9) * 6, (globals.CANVAS_DIMS[1] / 9) * 1))]
        self.Rocks = [Rock(((globals.CANVAS_DIMS[0] / 7) * 2, (globals.CANVAS_DIMS[1] / 3) * 1)),
                      Rock(((globals.CANVAS_DIMS[0] / 5) * 4, (globals.CANVAS_DIMS[1] / 5) * 3)),
                      Rock(((globals.CANVAS_DIMS[0] / 7) * 3, (globals.CANVAS_DIMS[1] / 3) * 2))]
        self.Gates = [Gate(3, 2, 1), Gate(0, 2, 3), Gate(1, 2, 4)]
        self.Room = Room()

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates, self.Rocks, self.Room)
        Levels.roomText = 3
