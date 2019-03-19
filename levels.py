try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from wheel import Wheel  # replace with player class
from keyboard import Keyboard
from playerInteraction import PlayerInteraction
from walls import Wall


class Levels:
    # static variable:
    player = Wheel()
    kbd = Keyboard()
    playerInteraction = PlayerInteraction(player, kbd)
    levels = []
    MeleeEnemies = []
    RangedEnemies = []
    Projectiles = []
    Walls = {Wall(0), Wall(1), Wall(2), Wall(3)}
    Gates = []
    GateInteractions = []

    def LoadLevel(self, meleeEnemiesList, rangedEnemiesList, gateList):
        Levels.MeleeEnemies = []
        Levels.RangedEnemies = []
        Levels.Projectiles = []
        for enemy in meleeEnemiesList:
            Levels.MeleeEnemies.append(enemy)
        for enemy in rangedEnemiesList:
            Levels.RangedEnemies.append(enemy)
        Levels.Gates = []
        for gate in gateList:
            Levels.Gates.append(gate)
        meleeEnemiesList = []
        rangedEnemiesList = []

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
        for gate in Levels.Gates:
            gate.update()

    @staticmethod
    def draw(canvas):
        Levels.player.draw(canvas)
        for melee in Levels.MeleeEnemies:
            melee.draw(canvas)
        for ranged in Levels.RangedEnemies:
            ranged.draw(canvas)
        for projectiles in Levels.Projectiles:
            projectiles.draw(canvas)
        for wall in Levels.Walls:
            wall.draw(canvas)
        for gate in Levels.Gates:
            gate.draw(canvas)
