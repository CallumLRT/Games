try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector


class PlayerInteraction:
    def __init__(self, player, keyboard, walls):
        self.player = player
        self.keyboard = keyboard
        self.walls = walls

    def update(self):
        if self.keyboard.up:
            if not (self.walls[0].distanceTo(self.player.pos) < self.walls[0].thickness + self.player.radius and
                    self.walls[0].covers(self.player.pos)):
                self.player.vel.add(Vector(0, -1))
            else:
                self.player.vel = Vector(0, 0)

        if self.keyboard.right:
            if not (self.walls[1].distanceTo(self.player.pos) < self.walls[1].thickness + self.player.radius and
                    self.walls[1].covers(self.player.pos)):
                self.player.vel.add(Vector(1, 0))
            else:
                self.player.vel = Vector(0, 0)

        if self.keyboard.down:
            if not (self.walls[2].distanceTo(self.player.pos) < self.walls[2].thickness + self.player.radius and
                    self.walls[2].covers(self.player.pos)):
                self.player.vel.add(Vector(0, 1))
            else:
                self.player.vel = Vector(0, 0)

        if self.keyboard.left:
            if not (self.walls[3].distanceTo(self.player.pos) < self.walls[3].thickness + self.player.radius and
                    self.walls[3].covers(self.player.pos)):
                self.player.vel.add(Vector(-1, 0))
            else:
                self.player.vel = Vector(0, 0)