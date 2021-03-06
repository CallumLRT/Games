try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from rock import Rock
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy
from gates import Gate
from room import Room
import globals


# stores values for level
class Level1(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = [MeleeEnemy(((globals.CANVAS_DIMS[0] / 9) * 5, (globals.CANVAS_DIMS[1] / 9) * 2)),
                             MeleeEnemy(((globals.CANVAS_DIMS[0] / 9) * 8, (globals.CANVAS_DIMS[1] / 9) * 7))]
        self.RangedEnemies = []
        self.Rocks = [Rock(((globals.CANVAS_DIMS[0] / 6) * 2, (globals.CANVAS_DIMS[1] / 8) * 3)),
                      Rock(((globals.CANVAS_DIMS[0] / 9) * 7, (globals.CANVAS_DIMS[1] / 5) * 4))]
        self.Gates = [Gate(0, 0, 1)]
        self.Room = Room()

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates, self.Rocks, self.Room)
        Levels.roomText = 1
