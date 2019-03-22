try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player
from interactions import Interaction
from keyboard import Keyboard
from playerInteraction import PlayerInteraction
from walls import Wall
from meleeInteractionSet import *
from room import Room


class Levels:
    # static variable:
    player = Player()
    kbd = Keyboard()
    room = Room()
    Walls = [Wall(0), Wall(1), Wall(2), Wall(3)]
    playerInteraction = PlayerInteraction(player, kbd, Walls)
    levels = []
    MeleeEnemies = []
    MeleeInteractions = []
    RangedEnemies = []
    Projectiles = []
    wall_interactions = []
    for wall in Walls:
        wall_interactions.append(Interaction(player, wall))
    Gates = []
    GateInteractions = []
    printText = 0

    def LoadLevel(self, meleeEnemiesList, rangedEnemiesList, gateList):
        Levels.MeleeEnemies = []
        Levels.RangedEnemies = []
        Levels.Projectiles = []
        Levels.MeleeInteractions = []
        for enemy in meleeEnemiesList:
            Levels.MeleeEnemies.append(enemy)
        for enemy in rangedEnemiesList:
            Levels.RangedEnemies.append(enemy)
        Levels.Gates = []
        for gate in gateList:
            Levels.Gates.append(gate)
        Levels.MeleeInteractions = MeleeInteractionSet(meleeEnemiesList)

    @staticmethod
    def update():
        Levels.player.update()
        Levels.playerInteraction.update()
        for interaction in Levels.wall_interactions:
            interaction.update()
        for melee in Levels.MeleeEnemies:
            melee.daze_cycle()
            if melee.currentlyTargeting:
                melee.target(Levels.player.pos)
            melee.update()
        Levels.MeleeInteractions.update()
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
        Levels.room.draw(canvas)
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
        canvas.draw_text(str(Levels.printText), (10, 15), 20, "White")
