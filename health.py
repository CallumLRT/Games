from enemy import Enemy
from globals import *
from scores import *

class Health:
    def __init__(self):
        self.health = 4

    def damaged(self, who, obj, rangedEnemies, meleeEnemies):
        self.health = self.health - 1
        if self.health == 0:
            if who == "RangedEnemy":
                rangedEnemies.remove(obj)
                Scores.score += 20
            elif who == "MeleeEnemy":
                meleeEnemies.remove(obj)
                Scores.score += 10
            else:
                print("Dead Player")
                Scores.score = 0
                pass
    '''
    def damaged(self):
        self.health = self.health - 1
        # if self.health == 0:
        #     #End game
        #     pass
        # check for game end is in menu.py in update()
    '''

    def gain(self):
        if self.health < 4:
            self.health = self.health + 1
