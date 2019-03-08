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

class Walls:
    def __init__(self):
        pass

    def draw(self, canvas):
        canvas.draw_line((0, 400), (0, 0), 20, 'red')
        canvas.draw_line((600, 0), (0, 0), 20, 'Red')
        canvas.draw_line((600, 0), (600, 400), 20, 'Red')
        canvas.draw_line((0, 400), (600, 400), 20, 'Red')