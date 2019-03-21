try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from spritesheet import SpriteSheet

class Player:
    def init(self):
        self.PlayerSprite = SpriteSheet('https://gyazo.com/616943d4546f31d854a59cc4b2b0b461', (3,4), i=0, j=0)

    def draw(self, canvas):
        self.PlayerSprite.draw(canvas)

    def update(self):
        while(#wkeypress)
            self.frameIndex = (0,0)
            self.PlayerSprite.nextFrameRows()
        while(#dkeypress)
            self.frameIndex = (1,0)
            self.PlayerSprite.nextFrameRows()
        while(#skeypress)
            self.frameIndex = (2,0)
            self.PlayerSprite.nextFrameRows()
        while(#akeypress)
            self.frameIndex = (3,0)
            self.PlayerSprite.nextFrameRows()
