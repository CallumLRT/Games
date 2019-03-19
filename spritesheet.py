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
    def init(self, url, frameWidth, frameHeight, dimX, dimY, x, y, i, j):
        # loading the image
        self.url = url
        self.img = simplegui.load_image(url)
        self.frameIndex = (0, 0)
        self.maxIndex = (i, j)
        self.frameWidth = self.img.get_width() / self.maxIndex[0]
        self.frameHeight = self.img.get_height() / self.maxIndex[1]
        self.frameCentreX = self.frameWidth/2
        self.frameCentreY = self.frameHeight/2
        x = self.frameWidth*self.frameIndex[0] + self.frameCentreX
        y = self.frameHeight*self.frameIndex[1] + self.frameCentreY

        # inside the drawing handler
        self.dimX = dimX
        self.dimY = dimY

    def draw(self, canvas):
        canvas.draw_image(
            self.img,
            (self.frameWidth*self.frameIndex[0]+self.frameCentreX, self.frameHeight*self.frameIndex[1]+self.frameCentreY),
            (self.frameWidth, self.frameHeight),
            (CANVAS_DIMS),
            (self.dimX, self.dimY)
        )

    def nextFrame(self):
        self.frameIndex = (self.frameIndex[0] + 1, self.frameIndex[1])


