try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player
from interactions import Interaction
from keyboard import Keyboard
from playerInteraction import PlayerInteraction
from walls import Wall
from interactionSet import *
from projectileCollision import ProjectileCollision
import globals
from scores import *

class Levels:
    # static variable:
    player = Player()  # the player
    kbd = Keyboard()  # keyboard class to check movement for player
    room = None # background for level
    Walls = [Wall(0), Wall(1), Wall(2), Wall(3)]  # all the walls
    playerInteraction = PlayerInteraction(player, kbd, Walls)  # interaction to keep player within the walls
    levels = []  # list of levels. levels get appended here when they load
    MeleeEnemies = []  # list of melee enemies
    ObjInteractions = []  # just initialising var to store interactions between melee enemies
    RangedEnemies = []  # list of ranged enemies
    Enemies = []
    Rocks = []  # List of rocks
    FriendlyProjectiles = []  # list of projectiles
    EnemyProjectiles = []
    wall_interactions = []  # list of wall interactions to help keep player within the walls
    for wall in Walls:
        wall_interactions.append(Interaction(player, wall))
    Gates = []  # list of gates to move player between levels
    GateInteractions = []  # list of interactions for above gates
    roomText = 0  # text to represent what room the player is in
    #scoreText = 0
    projectileCollision = ProjectileCollision(player)

    # called from within level# classes
    # meleeEnemiesList: the list of enemies from the level
    # rangedEnemiesList: the list of enemies from the level
    # gateList: list of gates from the level
    def LoadLevel(self, meleeEnemiesList, rangedEnemiesList, gateList, rockList, room):
        Levels.MeleeEnemies = []
        Levels.RangedEnemies = []
        Levels.Rocks = []
        Levels.FriendlyProjectiles = []
        Levels.EnemyProjectiles = []
        Levels.room = None
        Levels.ObjInteractions = []
        Levels.allObj = []
        Levels.Enemies = []
        Levels.Rocks = rockList
        for rock in rockList:
            Levels.allObj.append(rock)
        Levels.MeleeEnemies = meleeEnemiesList
        for enemy in meleeEnemiesList:
            Levels.allObj.append(enemy)
            Levels.Enemies.append(enemy)
        Levels.RangedEnemies = rangedEnemiesList
        for enemy in rangedEnemiesList:
            Levels.allObj.append(enemy)
            Levels.Enemies.append(enemy)
        Levels.Gates = []
        for gate in gateList:
            Levels.Gates.append(gate)
        Levels.room = room
        Levels.allObj.append(Levels.player)
        Levels.ObjInteractions.append(InteractionSet(Levels.allObj))

    @staticmethod
    def update():
        Levels.player.update()
        Levels.playerInteraction.update()
        if Levels.player.cooldown <= 0 and (
                Levels.kbd.arrow_up or Levels.kbd.arrow_right or Levels.kbd.arrow_down or Levels.kbd.arrow_left):
            Levels.FriendlyProjectiles.append(Levels.playerInteraction.shoot())
        for interaction in Levels.wall_interactions:
            interaction.update()
        for melee in Levels.MeleeEnemies:
            melee.daze_cycle()
            if melee.currentlyTargeting:
                melee.target(Levels.player.pos)
            melee.update()
        for interaction in Levels.ObjInteractions:
            interaction.update()
        for ranged in Levels.RangedEnemies:
            ranged.daze_cycle()
            if ranged.currentlyTargeting:
                ranged.target(Levels.player.pos)
            if ranged.cooldown <= 0:
                Levels.EnemyProjectiles.append(ranged.shoot(Levels.player.pos))
                #Levels.Projectiles.append(ranged.shoot(Levels.player.pos))
            ranged.update()
        for projectile in Levels.EnemyProjectiles:
            projectile.update()
            if projectile.frame_life <= 0:
                Levels.EnemyProjectiles.remove(projectile)
        for projectile in Levels.FriendlyProjectiles:
            projectile.update()
            if projectile.frame_life <= 0:
                Levels.FriendlyProjectiles.remove(projectile)
        for gate in Levels.Gates:
            gate.update()
        Levels.projectileCollision.update(Levels.EnemyProjectiles, Levels.FriendlyProjectiles, Levels.Rocks,
                                          Levels.RangedEnemies, Levels.MeleeEnemies)
        for enemy in Levels.MeleeEnemies:
            if Levels.player.collides(enemy) and enemy.currentlyAttacking:
                Levels.player.health.damaged("Player", Levels.player, Levels.RangedEnemies, Levels.MeleeEnemies)
                enemy.attacked()

    @staticmethod
    def draw(canvas):
        Levels.room.draw(canvas)
        Levels.player.draw(canvas)
        for rock in Levels.Rocks:
            rock.draw(canvas)
        for melee in Levels.MeleeEnemies:
            melee.draw(canvas)
        for ranged in Levels.RangedEnemies:
            ranged.draw(canvas)
        for projectiles in Levels.EnemyProjectiles:
            projectiles.draw(canvas)
        for projectiles in Levels.FriendlyProjectiles:
            projectiles.draw(canvas)
        for wall in Levels.Walls:
            wall.draw(canvas)
        for gate in Levels.Gates:
            gate.draw(canvas)
        canvas.draw_text("Room: " + str(Levels.roomText), (10, 9), 15, "White")
        canvas.draw_text("Score: " + str(Scores.score), (930, 9), 15, "White")

    @staticmethod
    def restart():
        Levels.player = Player()  # the player
        Levels.kbd = Keyboard()  # keyboard class to check movement for player
        Levels.room = None  # background for level
        Levels.Walls = [Wall(0), Wall(1), Wall(2), Wall(3)]  # all the walls
        Levels.playerInteraction = PlayerInteraction(Levels.player, Levels.kbd, Levels.Walls)  # interaction to keep player within the walls
        Levels.levels = []  # list of levels. levels get appended here when they load
        Levels.MeleeEnemies = []  # list of melee enemies
        Levels.ObjInteractions = []  # just initialising var to store interactions between melee enemies
        Levels.RangedEnemies = []  # list of ranged enemies
        Levels.Rocks = []  # List of rocks
        Levels.Projectiles = []  # list of projectiles
        Levels.wall_interactions = []  # list of wall interactions to help keep player within the walls
        for wall in Levels.Walls:
            Levels. wall_interactions.append(Interaction(Levels.player, wall))
        Levels.Gates = []  # list of gates to move player between levels
        Levels.GateInteractions = []  # list of interactions for above gates
        Levels.roomText = 0  # text to represent what room the player is in
        Scores.score = 0
