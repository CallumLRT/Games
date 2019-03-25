try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
from music import Music
from levels import Levels
from scores import *

CANVAS_DIMS = globals.CANVAS_DIMS


class Menu:
    def __init__(self):
        self.game_start = False
        self.game_end = False
        self.menu_music_playing = False
        self.won = False
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
        self.END_CENTRE = (self.END.get_width() / 2, self.END.get_height() / 2)
        self.END_DIMS = (self.END.get_width(), self.END.get_height())
        self.END_Size = (globals.CANVAS_DIMS[0]*0.7, globals.CANVAS_DIMS[0]*0.7)
        self.END_Pos = (globals.CANVAS_DIMS[0] / 2, globals.CANVAS_DIMS[1] / 2)  # where to draw image

        self.END_BUTT_Pos = (CANVAS_DIMS[0] / 2, (CANVAS_DIMS[1] / 6) * 5)


        self.WIN = simplegui.load_image(
            'https://raw.githubusercontent.com/CalhamZeKoala/GameImg/master/win.jpg')
        self.WIN_CENTRE = (self.WIN.get_width() / 2, self.WIN.get_height() / 2)
        self.WIN_DIMS = (self.WIN.get_width(), self.WIN.get_height())
        self.WIN_Size = (CANVAS_DIMS[0], CANVAS_DIMS[1])
        self.WIN_Pos = (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2)  # where to draw image

    def draw(self, canvas):
        if not self.game_start:
            canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.IMG_Pos,
                              self.IMG_Size)
            canvas.draw_image(self.BUTT, self.BUTT_CENTRE, self.BUTT_DIMS, self.BUTT_Pos,
                              self.BUTT_Size)
        if self.game_end:
            canvas.draw_image(self.END, self.END_CENTRE, self.END_DIMS, self.END_Pos,
                              self.END_Size)
            canvas.draw_image(self.BUTT, self.BUTT_CENTRE, self.BUTT_DIMS, self.END_BUTT_Pos,
                              self.BUTT_Size)
            canvas.draw_text("Score: " + str(Scores.score), (self.END_DIMS[0]/2 + 100, 50), 50, "White")
        if self.won:
            canvas.draw_image(self.WIN, self.WIN_CENTRE, self.WIN_DIMS, self.WIN_Pos,
                              self.WIN_Size)
            canvas.draw_image(self.BUTT, self.BUTT_CENTRE, self.BUTT_DIMS, self.END_BUTT_Pos,
                              self.BUTT_Size)
            canvas.draw_text("Score: " + str(Scores.score), (self.END_DIMS[0]/2 + 100, 50), 50, "White")


    def update(self):
        if not self.menu_music_playing and not self.game_start:
            self.menu_music.play()
            self.menu_music_playing = True
        if self.game_start and self.menu_music_playing and not self.game_end:
            self.menu_music.pause()
            self.menu_music.rewind()
            self.menu_music_playing = False
            self.game_music.play()
        if (self.game_end or self.won) and not self.menu_music_playing:
            self.game_music.pause()
            self.game_music.rewind()
            self.menu_music.play()
            self.menu_music_playing = True
            self.game_start = False
        if Levels.player.health.health <= 0:
            self.game_end = True
            self.game_start = True
        if len(Levels.Enemies) == 0 and self.game_start:
            self.won = True
