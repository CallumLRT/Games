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

one = Walls(Vector(0, 0), Vector(600, 0))

two = Walls(Vector(0, 0), Vector(0, 400))

three = Walls(Vector(0, 400), Vector(600, 400))

four = Walls(Vector(600, 0), Vector(600, 400))

class DrawWalls:
    def __init__(self):
        pass

    def get_walls(self):
        return [one, two, three, four]

    def draw(canvas):
        one.draw(canvas)
        two.draw(canvas)
        three.draw(canvas)
        four.draw(canvas)