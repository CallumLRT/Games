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
import globals

CANVAS_DIMS = globals.CANVAS_DIMS

def rotateAnti(v):
    return Vector(-v.y, v.x)

class Walls:
    def __init__(self, point1, point2):
        self.pA = point1
        self.pB = point2
        self.thickness = 20
        self.unit = (self.pB - self.pA).normalize()
        self.normal = rotateAnti(self.unit)

    def draw(self, canvas):
        canvas.draw_line(self.pA.getP(), self.pB.getP(), self.thickness, "red")

    def distanceTo(self, pos):
        posToA = pos - self.pA
        proj = posToA.dot(self.normal) * self.normal
        return proj.length()

    #    canvas.draw_line((0, 400), (0, 0), 20, 'red')
    #    canvas.draw_line((600, 0), (0, 0), 20, 'Red')
    #    canvas.draw_line((600, 0), (600, 400), 20, 'Red')
    #    canvas.draw_line((0, 400), (600, 400), 20, 'Red')