try:
    import simplegui
except ImportError:
    try:
        import simplegui2pygamemodule as simplegui
    except ImportError:
        try:
            import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
        except ImportError:
            print("rip")
            exit()

import globals

CANVAS_DIMS = globals.CANVAS_DIMS


class SpriteSheet:
    def init(self, url, frameWidth, frameHeight, dimX, dimY, x, y, maxIndex):
        # loading the image
        self.url = url
        self.img = simplegui.load_image(url)
        self.frameIndex = (0, 0)
        self.maxIndex = maxIndex
        self.frameWidth = self.img.get_width() / self.maxIndex[0]
        self.frameHeight = self.img.get_height() / self.maxIndex[1]
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        x = self.frameWidth * self.frameIndex[0] + self.frameCentreX
        y = self.frameHeight * self.frameIndex[1] + self.frameCentreY
        self.pos = (x, y)

        # inside the drawing handler
        self.dimX = dimX
        self.dimY = dimY

    def draw(self, canvas):
        canvas.draw_image(
            self.img,
            (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
             self.frameHeight * self.frameIndex[1] + self.frameCentreY),
            (self.frameWidth, self.frameHeight),
            self.pos,
            (self.dimX, self.dimY)
        )

    def nextFrame(self):
        self.frameIndex = (self.frameIndex[0] + 1, self.frameIndex[1])
        if self.frameIndex[0] >= self.maxIndex[0]:
            self.frameIndex = (0, self.frameIndex[1] + 1)
        if self.frameIndex[1] >= self.maxIndex[1]:
            self.frameIndex = (0, 0)
        print(self.frameIndex)