try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from wheel import Wheel  # replace with player class
from keyboard import Keyboard
from playerInteraction import PlayerInteraction


class Levels:
    # static variable:
    player = Wheel()
    kbd = Keyboard()
    playerInteraction = PlayerInteraction(player, kbd)
    levels = []
    MeleeEnemies = []
    RangedEnemies = []
    Projectiles = []
    Gates = []
    GateInteractions = []

    # moved to update()
    # @staticmethod
    # def enemy_shoot():
    #     for enemy in Levels.RangedEnemies:
    #         enemy.target(Levels.player.pos)
    #         if enemy.cooldown <= 0:
    #             Levels.Projectiles.append(enemy.shoot(Levels.player.pos))

    @staticmethod
    def update():
        Levels.player.update()
        Levels.playerInteraction.update()
        for melee in Levels.MeleeEnemies:
            melee.target(Levels.player.pos)
            melee.update()
        for ranged in Levels.RangedEnemies:
            ranged.target(Levels.player.pos)
            ranged.update()
            if ranged.cooldown <= 0:
                Levels.Projectiles.append(ranged.shoot(Levels.player.pos))
        for projectile in Levels.Projectiles:
            projectile.update()
            if projectile.frame_life <= 0:
                Levels.Projectiles.remove(projectile)

    @staticmethod
    def draw(canvas):
        Levels.player.draw(canvas)
        for melee in Levels.MeleeEnemies:
            melee.draw(canvas)
        for ranged in Levels.RangedEnemies:
            ranged.draw(canvas)
        for projectiles in Levels.Projectiles:
            projectiles.draw(canvas)
