try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals

from vector import Vector
from interactions import Interaction
from walls import Wall
from levels import Levels
from level1 import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4
from level5 import Level5
from menu import Menu
from music import Music

# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

menu = Menu()

level1 = Level1()
level2 = Level2()
level3 = Level3()
level4 = Level4()
level5 = Level5()

gameMusic = Music(
    "https://raw.githubusercontent.com/CalhamZeKoala/Games/master/music/DungeonMusic.ogg?token=AuVrB4f-o_7jKhvx9o8zywf9tICgCGp_ks5coU0IwA%3D%3D")

menuMusic = Music(
    "https://raw.githubusercontent.com/CalhamZeKoala/Games/master/music/LobbyMusic.ogg?token=AuVrB01tDWNIZM_FEJe1dp2X42W41OC7ks5coVI9wA%3D%3D")
menuMusic.play()


def draw(canvas):
    if menu.game_start:
        Levels.update()
        Levels.draw(canvas)
    else:
        menu.draw(canvas)


def mouse_handler(pos):
    if menu.BUTT_Pos[0] - menu.BUTT_CENTRE[0] <= pos[0] <= menu.BUTT_Pos[0] + menu.BUTT_CENTRE[0]:
        if menu.BUTT_Pos[1] - menu.BUTT_CENTRE[1] <= pos[1] <= menu.BUTT_Pos[1] + menu.BUTT_CENTRE[1]:
            level1.LoadLevel()
            menu.game_start = True
            menuMusic.pause()
            gameMusic.play()


frame = simplegui.create_frame('Game', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('black')
frame.set_draw_handler(draw)
frame.set_keydown_handler(Levels.kbd.keyDown)
frame.set_keyup_handler(Levels.kbd.keyUp)
frame.set_mouseclick_handler(mouse_handler)
frame.start()
