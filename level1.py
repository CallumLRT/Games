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
        self.MeleeEnemies = [MeleeEnemy((globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 4))]
        self.RangedEnemies = []
        self.Rocks = [Rock((globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 4))]
        self.Gates = [Gate(0, 0, 1)]
        self.Room = Room()

    def LoadLevel(self):
        super().LoadLevel(self.MeleeEnemies, self.RangedEnemies, self.Gates, self.Rocks, self.Room)
        Levels.printText = 1
