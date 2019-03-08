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
from wheel import Wheel
import globals

CANVAS_DIMS = globals.CANVAS_DIMS

wheel = Wheel()
walls = Walls()

class Interactions:
    def __init__(self):
        pass

    def checkCollisionWith(self, other):


