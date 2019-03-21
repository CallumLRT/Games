try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
from vector import Vector
from playerInteraction import PlayerInteraction
from keyboard import Keyboard
from wheel import Wheel
from meleeEnemy import MeleeEnemy
from rangedEnemy import RangedEnemy
from interactions import Interaction
from walls import Wall
from player import Player

# constants
# add them in the global files so they can be used across multiple files
CANVAS_DIMS = globals.CANVAS_DIMS

kbd = Keyboard()
wheel = Player()
playerInter = PlayerInteraction(wheel, kbd)

walls = []
walls.append(Wall(Vector(0, 0), Vector(CANVAS_DIMS[0], 0), Vector(0, 1)))
walls.append(Wall(Vector(CANVAS_DIMS[0], 0), Vector(CANVAS_DIMS[0], CANVAS_DIMS[1]), Vector(-1, 0)))
walls.append(Wall(Vector(0, CANVAS_DIMS[1]), Vector(CANVAS_DIMS[0], CANVAS_DIMS[1]), Vector(0, -1)))
walls.append(Wall(Vector(0, 0), Vector(0, CANVAS_DIMS[1]), Vector(1, 0)))

wall_interactions = []
for wall in walls:
    wall_interactions.append(Interaction(wheel, wall))

melee_enemies = []
melee_enemies.append(MeleeEnemy((500, 100)))
melee_enemies.append(MeleeEnemy((100, 100)))
ranged_enemies = []
ranged_enemies.append(RangedEnemy((100, 100)))
fireballs = []


def draw(canvas):
    for wall in walls:
        wall.draw(canvas)
    for interaction in wall_interactions:
        interaction.update()
    playerInter.update()
    wheel.update()
    wheel.draw(canvas)
    for enemy in melee_enemies:
        enemy.draw(canvas)
        enemy.target(wheel.pos)
        enemy.update()
    for enemy in ranged_enemies:
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


frame = simplegui.create_frame('Game', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('black')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
