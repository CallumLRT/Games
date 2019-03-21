try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
import globals


class Wall:
    def __init__(self, side):
        if side == 0:  # top of the map
            self.pA = Vector(0, 0)
            self.pB = Vector(globals.CANVAS_DIMS[0], 0)
            self.direction_of_player = Vector(0, 1)
        elif side == 1:  # right side
            self.pA = Vector(globals.CANVAS_DIMS[0], 0)
            self.pB = Vector(globals.CANVAS_DIMS[0], globals.CANVAS_DIMS[1])
            self.direction_of_player = Vector(-1, 0)
        elif side == 2:  # bottom side
            self.pA = Vector(0, globals.CANVAS_DIMS[1])
            self.pB = Vector(globals.CANVAS_DIMS[0], globals.CANVAS_DIMS[1])
            self.direction_of_player = Vector(0, -1)
        elif side == 3:  # right side
            self.pA = Vector(0, 0)
            self.pB = Vector(0, globals.CANVAS_DIMS[1])
            self.direction_of_player = Vector(1, 0)
        self.thickness = 20
        self.unit = (self.pB - self.pA).normalize()
        self.normal = Vector(-self.unit.y, self.unit.x)

    def draw(self, canvas):
        canvas.draw_line(self.pA.get_p(), self.pB.get_p(), self.thickness, "Red")

    def distanceTo(self, pos):
        posToA = pos - self.pA
        proj = posToA.dot(self.normal) * self.normal
        return proj.length()

    def covers(self, pos):
        return ((pos - self.pA).dot(self.unit) >= 0 and
                (pos - self.pB).dot(-self.unit) >= 0)
