try:
    import simplegui
except ImportError:
    try:
        import simplegui2pygamemodule as simplegui
    except ImportError:
        try:
            import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
        except ImportError:
            print("R.I.P")
            exit()

from vector import Vector
from walls import Walls
from drawWalls import DrawWalls
from wheel import Wheel
import globals

CANVAS_DIMS = globals.CANVAS_DIMS

wheel = Wheel()
#walls = Walls()

class Interactions:
    def __init__(self, wheel):
        self.wheel = wheel
        self.walls = DrawWalls()
        self.inCollision = False

    def distance_to_walls(self, pos):
        allWalls = self.walls.get_walls()
        distances = []
        for i in allWalls:
            distances.append((i.pos-pos).length())
        return distances

    def update(self):
        if (self.distance_to_walls(self.wheel.pos) < self.walls.thickness + self.wheel.imgRadius and self.line.covers(self.wheel.pos)):
            if not self.inCollision:
                self.wheel.bounce(self.wheel.normal)
                self.inCollision = True
            else:
                self.inCollision = False


