try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# adapted from the code provided in lectures

# TODO: prevent player from jittering when touching the wall
class Interaction:
    def __init__(self, particle, line):
        self.particle = particle
        self.line = line
        self.inCollision = False
        self.line.direction_of_player.multiply(5)

    def update(self):
        if (self.line.distanceTo(self.particle.pos) < self.line.thickness + self.particle.radius and
                self.line.covers(self.particle.pos)):
            if not self.inCollision:
                # self.particle.vel.reflect(self.line.normal) # this bounces the particle from the wall
                self.particle.vel = self.particle.vel.subtract(self.particle.vel)  # this stops the particle
                self.inCollision = True
            else:
                self.particle.pos.add(self.line.direction_of_player)
        else:
            self.inCollision = False
