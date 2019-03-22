try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    
# Don't touch this anymore
class SpriteSheet:
    # url: url for image
    # maxIndex: how many (columns,rows) there are in the spritesheet
    # frameDelay: delay in between frames to slow down the animation
    def __init__(self, url, maxIndex, frameDelay=1):
        self.url = url
        self.img = simplegui.load_image(url)
        self.index = (0, 0)
        self.maxIndex = maxIndex
        self.frameWidth = self.img.get_width() / maxIndex[0]
        self.frameHeight = self.img.get_height() / maxIndex[1]
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.frameDelay = frameDelay
        self.frame = 0

    # pos: the (x, y) coordinates to draw at
    def draw(self, canvas, pos):
        canvas.draw_image(self.img,
                          (self.frameWidth * self.index[0] + self.frameCentreX,
                           self.frameHeight * self.index[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight),
                          (pos[0], pos[1]),
                          (self.frameWidth, self.frameHeight)
                          )

    def update(self):
        self.frame += 1
        if self.frame == self.frameDelay:
            self.index = (self.index[0] + 1, self.index[1])
            if self.index[0] >= self.maxIndex[0]:
                self.index = (0, self.index[1] + 1)
            if self.index[1] >= self.maxIndex[1]:
                self.index = (0, 0)
            self.frame = 0
