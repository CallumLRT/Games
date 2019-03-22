try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from vector import Vector
import globals


class Gate():
    # side: number representing which side to put wall on (0=top, 1=right, 2=bottom, 3=left)
    # currentLevelIndex = the index of the level in Levels.levels (this is usually level#-1)
    # nextLevelIndex = the index of the level in Levels.levels (this is usually level#-1)
    def __init__(self, side, currentLevelIndex, nextLevelIndex):
        self.currentLevelIndex = currentLevelIndex
        self.nextLevelIndex = nextLevelIndex
        self.thickness = 35
        if side == 0:  # top of the map
            self.pA = Vector((globals.CANVAS_DIMS[0] / 5) * 2, 0)
            self.pB = Vector((globals.CANVAS_DIMS[0] / 5) * 3, 0)
            self.exitPos = Vector(globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] - (Levels.player.radius * 3))
        elif side == 1:  # right side
            self.pA = Vector(globals.CANVAS_DIMS[0], (globals.CANVAS_DIMS[1] / 5) * 2)
            self.pB = Vector(globals.CANVAS_DIMS[0], (globals.CANVAS_DIMS[1] / 5) * 3)
            self.exitPos = Vector((Levels.player.radius * 3), globals.CANVAS_DIMS[1] / 2)
        elif side == 2:  # bottom side
            self.pA = Vector((globals.CANVAS_DIMS[0] / 5) * 2, globals.CANVAS_DIMS[1])
            self.pB = Vector((globals.CANVAS_DIMS[0] / 5) * 3, globals.CANVAS_DIMS[1])
            self.exitPos = Vector(globals.CANVAS_DIMS[0] / 2, (Levels.player.radius * 3))
        elif side == 3:  # left side
            self.pA = Vector(0, (globals.CANVAS_DIMS[1] / 5) * 2)
            self.pB = Vector(0, (globals.CANVAS_DIMS[1] / 5) * 3)
            self.exitPos = Vector(globals.CANVAS_DIMS[0] - (Levels.player.radius * 3), globals.CANVAS_DIMS[1] / 2)
        self.unit = (self.pB - self.pA).normalize()
        self.normal = Vector(-self.unit.y, self.unit.x)

    # pos: coordinates to measure to
    def distanceTo(self, pos):
        posToA = pos - self.pA
        proj = posToA.dot(self.normal) * self.normal
        return proj.length()

    # pos: coordinates to check
    def covers(self, pos):
        return ((pos - self.pA).dot(self.unit) >= 0 and
                (pos - self.pB).dot(-self.unit) >= 0)

    # draw function
    def draw(self, canvas):
        canvas.draw_line(self.pA.get_p(), self.pB.get_p(), self.thickness, "Black")

    # update function
    def update(self):
        if (self.distanceTo(Levels.player.pos) < self.thickness + Levels.player.radius and
                self.covers(Levels.player.pos)):
            Levels.levels[self.nextLevelIndex].LoadLevel()
            Levels.player.pos = self.exitPos.copy()
