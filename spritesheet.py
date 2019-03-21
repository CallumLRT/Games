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
    def init(self, url, maxIndex, i=0, j=0):
        # loading the image
        self.url = url
        self.img = simplegui.load_image(url)
        self.frameIndex = (0, 0)
        self.maxIndex = maxIndex
        self.frameWidth = self.img.get_width() / self.maxIndex[0]
        self.frameHeight = self.img.get_height() / self.maxIndex[1]
        self.frameCentreX = self.frameWidth/2
        self.frameCentreY = self.frameHeight/2
        self.x = self.frameWidth*self.frameIndex[0] + self.frameCentreX
        self.y = self.frameHeight*self.frameIndex[1] + self.frameCentreY
        self.i = i
        self.j = j
        self.pos = (i, j)

    def draw(self, canvas):
        canvas.draw_image(
            self.img,
            (self.frameWidth*self.frameIndex[0]+self.frameCentreX, self.frameHeight*self.frameIndex[1]+self.frameCentreY),
            (self.frameWidth, self.frameHeight),
            (self.pos),
            (self.frameWidth, self.frameHeight)
        )

    def nextFrame(self):
        self.frameIndex = (self.frameIndex[0] + 1, self.frameIndex[1])
        if self.frameIndex[0] >= self.maxIndex[0]:
            self.frameIndex = (0, self.frameIndex[1] + 1)
        if self.frameIndex[1] >= self.maxIndex[1]:
            self.frameIndex = (0, 0)
        print(self.frameIndex)

    def nextFrameRows(self):
        self.frameIndex = (self.frameIndex[0] + 1, self.frameIndex[1])
        if self.frameIndex[0] >= self.maxIndex[0]:
            self.frameIndex = (0, self.frameIndex[1])
