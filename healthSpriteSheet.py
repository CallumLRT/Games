try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from spritesheet import SpriteSheet
import globals


class HealthSpriteSheet(SpriteSheet):
    def __init__(self, healthClass):
        super().__init__(
            "https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/heartspritesupdated.png",
            (1, 5))
        self.healthClass = healthClass

    def update(self):
        self.index = [0, (self.maxIndex[1] - 1) - self.healthClass.health]

    def draw(self, canvas):
        super().draw(canvas, ((self.frameWidth / 2) + 10, globals.CANVAS_DIMS[1] - 35))
