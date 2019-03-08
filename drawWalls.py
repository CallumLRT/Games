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
import globals

CANVAS_DIMS = globals.CANVAS_DIMS

one = Walls(Vector((0, 400), (0, 0)), Vector((600, 0), (0, 0)))

two = Walls(Vector((600, 0), (600, 400)), Vector((0, 400), (600, 400)))

class DrawWalls:
    def __init__(self):
        pass

    def draw(self,canvas):
        one.draw(canvas)
        two.draw(canvas)