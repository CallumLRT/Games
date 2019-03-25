class Health:
    def __init__(self):
        self.health = 4


    def damaged(self):
        self.health = self.health - 1
        # if self.health == 0:
        #     #End game
        #     pass
        # check for game end is in menu.py in update()

    def gain(self):
        if self.health < 4:
            self.health = self.health + 1
