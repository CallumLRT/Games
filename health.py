from enemy import Enemy

class Health:
    def __init__(self):
        self.health = 4

    def damaged(self, who, obj, rangedEnemies, meleeEnemies):
        self.health = self.health - 1
        if self.health == 0:
            if who == "RangedEnemy":
                rangedEnemies.remove(obj)
            elif who == "MeleeEnemy":
                meleeEnemies.remove(obj)
            else:
                print("Dead Player")
                pass

    def gain(self):
        if self.health < 4:
            self.health = self.health + 1
