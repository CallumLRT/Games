try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Music:

    def __init__(self):
        self.music = simplegui.load_sound(
            "https://raw.githubusercontent.com/CalhamZeKoala/Games/master/music/DungeonMusic.ogg?token=AuVrB4f-o_7jKhvx9o8zywf9tICgCGp_ks5coU0IwA%3D%3D")
        self.music.set_volume(0.1)

    # Event Handlers
    def play(self):
        self.music.play()

    def pause(self):
        self.music.pause()

