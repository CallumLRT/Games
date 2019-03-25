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
class Level5(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = [MeleeEnemy((globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 2))]
        self.RangedEnemies = []
        self.Rocks = [Rock(((globals.CANVAS_DIMS[0] / 6) * 1, (globals.CANVAS_DIMS[1] / 8) * 6)),
                      Rock(((globals.CANVAS_DIMS[0] / 9) * 4, (globals.CANVAS_DIMS[1] / 8) * 5))]
        self.Gates = [Gate(3, 4, 2)]
        self.Room = Room()

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates, self.Rocks, self.Room)
        Levels.roomText = 5
