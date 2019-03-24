class Health:
    def __init__(self):
        self.health = 4

    def damaged(self):
        self.health = self.health - 1
        if self.health == 0:
            #End game
            pass

    def gain(self):
        if self.health < 4:
            self.health = self.health + 1
