try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from spritesheet import SpriteSheet


class HealthSpriteSheet(SpriteSheet):
    def __init__(self):
        super().__init__(
            "https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/heartspritesupdated.png",
            (1, 5))

    def update(self, health):
        self.index = [0, (self.maxIndex[1] - 1) - health]
