try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# Don't touch this anymore
class SpriteSheet:
    def __init__(self, url, maxIndex):
        self.url = url
        self.img = simplegui.load_image(url)
        self.index = (0, 0)
        self.maxIndex = maxIndex
        self.frameWidth = self.img.get_width() / maxIndex[0]
        self.frameHeight = self.img.get_height() / maxIndex[1]
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2

    def draw(self, canvas, pos):
        canvas.draw_image(self.img,
                          (self.frameWidth * self.index[0] + self.frameCentreX,
                           self.frameHeight * self.index[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight),
                          (pos[0] + self.frameCentreX, pos[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight)
                          )

    def nextFrame(self):
        self.index = (self.index[0] + 1, self.index[1])
        if self.index[0] >= self.maxIndex[0]:
            self.index = (0, self.index[1] + 1)
        if self.index[1] >= self.maxIndex[1]:
            self.index = (0, 0)
