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
        # self.PlayerSprite = SpriteSheet('https://gyazo.com/616943d4546f31d854a59cc4b2b0b461', (3, 4))
        self.PlayerSprite_up = SpriteSheet(
            "https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/player%20sprites/player_up.png",
            (4, 1), 10)
        self.PlayerSprite_right = SpriteSheet(
            "https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/player%20sprites/player_right.png",
            (4, 1), 10)
        self.PlayerSprite_down = SpriteSheet(
            "https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/player%20sprites/player_down.png",
            (4, 1), 10)
        self.PlayerSprite_left = SpriteSheet(
            "https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/player%20sprites/player_left.png",
            (4, 1), 10)
        self.PlayerSprite_current = self.PlayerSprite_up
        self.vel = Vector(3, 0)
        self.pos = Vector(CANVAS_DIMS[0] / 2, 2 * CANVAS_DIMS[1] / 3.)
        self.radius = max(self.PlayerSprite_current.frameHeight, self.PlayerSprite_current.frameWidth) / 2

    def draw(self, canvas):
        self.PlayerSprite_current.draw(canvas, self.pos.get_p())

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.7)
        self.PlayerSprite_current.update()
