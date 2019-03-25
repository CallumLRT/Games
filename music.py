try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Music:

    def __init__(self, url):
        self.music = simplegui.load_sound(url)
        self.music.set_volume(0.1)

    # Event Handlers
    def play(self):
        self.music.play()

    def pause(self):
        self.music.pause()

    def rewind(self):
        self.music.rewind()
