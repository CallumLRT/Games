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
    player = Player()  # the player
    kbd = Keyboard()  # keyboard class to check movement for player
    room = Room()  # background for level
    Walls = [Wall(0), Wall(1), Wall(2), Wall(3)]  # all the walls
    playerInteraction = PlayerInteraction(player, kbd, Walls)  # interaction to keep player within the walls
    levels = []  # list of levels. levels get appended here when they load
    MeleeEnemies = []  # list of melee enemies
    MeleeInteractions = None  # just initialising var to store interactions between melee enemies
    RangedEnemies = []  # list of ranged enemies
    Projectiles = []  # list of projectiles
    wall_interactions = []  # list of wall interactions to help keep player within the walls
    for wall in Walls:
        wall_interactions.append(Interaction(player, wall))
    Gates = []  # list of gates to move player between levels
    GateInteractions = []  # list of interactions for above gates
    printText = 0  # text to represent what level the player is on

    # called from within level# classes
    # meleeEnemiesList: the list of enemies from the level
    # rangedEnemiesList: the list of enemies from the level
    # gateList: list of gates from the level
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
        if Levels.player.cooldown <= 0 and (
                Levels.kbd.arrow_up or Levels.kbd.arrow_right or Levels.kbd.arrow_down or Levels.kbd.arrow_left):
            Levels.Projectiles.append(Levels.playerInteraction.shoot())
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
