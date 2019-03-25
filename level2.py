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
class Level2(Levels):
    def __init__(self):
        Levels.levels.append(self)
        self.MeleeEnemies = [MeleeEnemy((globals.CANVAS_DIMS[0] / 3, globals.CANVAS_DIMS[1] / 2)),
                             MeleeEnemy(((globals.CANVAS_DIMS[0] / 3 * 2), globals.CANVAS_DIMS[1] / 2))]
        self.RangedEnemies = [RangedEnemy((globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 2))]
        self.Rocks = [Rock(((globals.CANVAS_DIMS[0] / 3) * 2, (globals.CANVAS_DIMS[1] / 2))),
                      Rock(((globals.CANVAS_DIMS[0] / 9) * 7, (globals.CANVAS_DIMS[1] / 5) * 2)),
                      Rock(((globals.CANVAS_DIMS[0] / 7) * 2, (globals.CANVAS_DIMS[1] / 6) * 5)),
                      Rock(((globals.CANVAS_DIMS[0] / 5) * 3, (globals.CANVAS_DIMS[1] / 9) * 2))]
        self.Gates = [Gate(2, 1, 0), Gate(1, 1, 2)]
        self.Room = Room()

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates, self.Rocks, self.Room)
        Levels.roomText = 2
