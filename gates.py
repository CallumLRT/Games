try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels


class gate():
    def __init__(self, Level1, Level2):
        self.level1 = Level1
        self.level2 = Level2
