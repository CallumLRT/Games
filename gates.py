try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from vector import Vector
import globals


class gate():
    def __init__(self, side, Level1Index, Level2Index):
        self.level1 = Levels.levels[Level1Index]
        self.level2 = Levels.levels[Level2Index]
        if side == 0:  # top of the map
            self.pA = Vector((globals.CANVAS_DIMS[0] / 5) * 2, 0)
            self.pB = Vector((globals.CANVAS_DIMS[0] / 5) * 3, 0)
        # elif side == 1:  # right side
        #     self.pA = Vector((globals.CANVAS_DIMS[0] / 5) * 2, 0)
        #     self.pB = Vector((globals.CANVAS_DIMS[0] / 5) * 3, 0)
        # elif side == 1:  # right side
        #     self.pA = Vector((globals.CANVAS_DIMS[0] / 5) * 2, 0)
        #     self.pB = Vector((globals.CANVAS_DIMS[0] / 5) * 3, 0)
        # elif side == 1:  # right side
        #     self.pA = Vector((globals.CANVAS_DIMS[0] / 5) * 2, 0)
        #     self.pB = Vector((globals.CANVAS_DIMS[0] / 5) * 3, 0)
        self.thickness = 20

    def distanceTo(self, pos):
        posToA = pos - self.pA
        proj = posToA.dot(self.normal) * self.normal
        return proj.length()

    def covers(self, pos):
        return ((pos - self.pA).dot(self.unit) >= 0 and
                (pos - self.pB).dot(-self.unit) >= 0)

    def draw(self, canvas):
        canvas.draw_line(self.pA.get_p(), self.pB.get_p(), self.thickness, "Black")
