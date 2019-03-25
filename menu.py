try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
import random
from music import Music
from levels import Levels

CANVAS_DIMS = globals.CANVAS_DIMS


class Menu:
    def __init__(self):
        self.game_start = False
        self.game_end = False
        self.menu_music_playing = False
        self.game_music = Music(
            "https://raw.githubusercontent.com/CalhamZeKoala/Games/master/music/DungeonMusic.ogg?token=AuVrB4f-o_7jKhvx9o8zywf9tICgCGp_ks5coU0IwA%3D%3D")

        self.menu_music = Music(
            "https://raw.githubusercontent.com/CalhamZeKoala/Games/master/music/LobbyMusic.ogg?token=AuVrB01tDWNIZM_FEJe1dp2X42W41OC7ks5coVI9wA%3D%3D")

        self.IMG = simplegui.load_image(
            'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Simple_grey.png?token=AexQrWRp93DDGdtspxKgQRIo_NppOK6Gks5coMbQwA%3D%3D')
        self.IMG_CENTRE = (self.IMG.get_width() / 2, self.IMG.get_height() / 2)
        self.IMG_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.IMG_Size = (CANVAS_DIMS[0], CANVAS_DIMS[1])
        self.IMG_Pos = (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2)  # where to draw image

        self.BUTT = simplegui.load_image(
            'https://raw.githubusercontent.com/CalhamZeKoala/Games/master/images/Start_button.png?token=AexQrbMnYHDhtdp3TYrgjTkO46pzViXQks5coMtLwA%3D%3D')
        self.BUTT_CENTRE = (self.BUTT.get_width() / 2, self.BUTT.get_height() / 2)
        self.BUTT_DIMS = (self.BUTT.get_width(), self.BUTT.get_height())
        self.BUTT_Size = self.BUTT_DIMS
        self.BUTT_Pos = (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2)  # where to draw image

        self.END = simplegui.load_image(
            'https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/gameover.jpg')
        self.END_CENTRE = (self.IMG.get_width() / 2, self.IMG.get_height() / 2)
        self.END_DIMS = (self.IMG.get_width(), self.IMG.get_height())
        self.END_Size = self.IMG_DIMS
        self.END_Pos = (globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 2)  # where to draw image

    def draw(self, canvas):
        if not self.game_start:
            canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.IMG_Pos,
                              self.IMG_Size)
            canvas.draw_image(self.BUTT, self.BUTT_CENTRE, self.BUTT_DIMS, self.BUTT_Pos,
                              self.BUTT_Size)
        if self.game_end:
            canvas.draw_image(self.END, self.END_CENTRE, self.END_DIMS, self.END_Size,
                              self.END_Pos)

    def update(self):
        if not self.menu_music_playing and not self.game_start:
            self.menu_music.play()
            self.menu_music_playing = False
        if self.game_start and self.menu_music_playing:
            self.menu_music.pause()
            self.menu_music.rewind()
            self.menu_music_playing = False
            self.game_music.play()
        if self.game_end:
            self.game_music.pause()
            self.game_music.rewind()
            self.menu_music.play()
            self.menu_music_playing = True
        if Levels.player.health.health <= 0:
            self.game_end = True
            self.game_start = False
