try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from spritesheet import SpriteSheet
import globals

CANVAS_DIMS = globals.CANVAS_DIMS


class Player:
    def __init__(self):
        #self.PlayerSprite = SpriteSheet('https://gyazo.com/616943d4546f31d854a59cc4b2b0b461', (3, 4))
        self.PlayerSprite = SpriteSheet("http://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png", (9,9))
        self.vel = Vector(3, 0)
        self.pos = Vector(CANVAS_DIMS[0] / 2, 2 * CANVAS_DIMS[1] / 3.)
        self.radius = max(self.PlayerSprite.frameHeight, self.PlayerSprite.frameWidth) / 2

    def draw(self, canvas):
        self.PlayerSprite.draw(canvas, self.pos.get_p())

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.9)
        self.PlayerSprite.update()
        # while (  # wkeypress)
        #         self.frameIndex = (0, 0)
        # self.PlayerSprite.nextFrameRows()
        # while (  # dkeypress)
        #         self.frameIndex = (1, 0)
        # self.PlayerSprite.nextFrameRows()
        # while (  # skeypress)
        #         self.frameIndex = (2, 0)
        # self.PlayerSprite.nextFrameRows()
        # while (  # akeypress)
        #         self.frameIndex = (3, 0)
        # self.PlayerSprite.nextFrameRows()
