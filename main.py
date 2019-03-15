try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
from interaction import Interaction
from keyboard import Keyboard
from wheel import Wheel
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy


# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

kbd = Keyboard()
wheel = Wheel()
inter = Interaction(wheel, kbd)
enemy = RangedEnemy((100, 100))
fireballs = []

enemies = []
enemies.append(MeleeEnemy((500, 100)))
enemies.append(MeleeEnemy((100, 100)))


def draw(canvas):
    inter.update()
    wheel.update()
    wheel.draw(canvas)
    enemy.update()
    enemy.draw(canvas)
    enemy.target(wheel.pos)
    if enemy.cooldown <= 0:
        fireballs.append(enemy.shoot(wheel.pos))
    for fireball in fireballs:
        fireball.update()
        fireball.draw(canvas)
        if fireball.frame_life <= 0:
            fireballs.remove(fireball)
    for enemy in enemies:
        enemy.draw(canvas)
        enemy.target(wheel.pos)
        enemy.update()


frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('black')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
