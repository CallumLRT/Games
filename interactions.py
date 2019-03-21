try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector


# adapted from the code provided in lectures

# works together wil PlayerInteractions class
# PlayerInteractions prevents moving into wall
# this class prevents excess velocity of player pushing them through the wall
class Interaction:
    def __init__(self, particle, line):
        self.particle = particle
        self.line = line
        self.inCollision = False
        self.line.direction_of_player.multiply(5)

    def update(self):
        if (self.line.distanceTo(self.particle.pos) < self.line.thickness + self.particle.radius - 1 and
                self.line.covers(self.particle.pos)):
            if not self.inCollision:
                self.inCollision = True
            else:
                self.particle.pos.add(self.line.direction_of_player)
                self.particle.vel = Vector(0, 0)
        else:
            self.inCollision = False
