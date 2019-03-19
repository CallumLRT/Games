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
    def init(self, url, frameWidth, frameHeight, dimX, dimY):
        # loading the image
        self.url = url
        self.img = simplegui.load_image(url)
        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        self.frameCentreX = self.frameWidth/2
        self.frameCentreY = self.frameHeight/2
        self.frameIndex = (i,j)
        x = self.frameWidth*frameIndex[0] + self.frameCentreX
        y = self.frameHeight*frameIndex[1] + self.frameCentreY

        # inside the drawing handler
        self.dimX = dimsX
        self.dimY = dimsY

    def draw(self, canvas):
        canvas.draw_image(
            self.img,
            (self.frameWidth*self.frameIndex[0]+self.frameCentreX, self.frameHeight*self.frameIndex[1]+self.frameCentreY),
            (self.frameWidth, self.frameHeight),
            (CANVAS_DIMS),
            (self.dimX, self.dimY)
        )

    def nextFrame(self):
        self.index = (self.index[0] + 1, self.index[1])

