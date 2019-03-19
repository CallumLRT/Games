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
    def init(self, url, frameWidth, frameHeight, dimX, dimY, rows, columns):
        # loading the image
        self.url = url
        self.img = simplegui.load_image(url)
        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        self.frameCentreX = self.frameWidth/2
        self.frameCentreY = self.frameHeight/2
        self.frameIndex = (i,j)
        rows = self.frameWidth*frameIndex[0] + self.frameCentreX
        columns = self.frameHeight*frameIndex[1] + self.frameCentreY

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


