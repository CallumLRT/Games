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
            self.player.PlayerSprite_current = self.player.PlayerSprite_up
            self.player.PlayerSprite_current.update()
            if not (self.walls[0].distanceTo(self.player.pos) < self.walls[0].thickness + self.player.radius + 1 and
                    self.walls[0].covers(self.player.pos)):
                self.player.vel.add(Vector(0, -1))
            else:
                self.player.vel = Vector(0, 0)

        if self.keyboard.down:
            self.player.PlayerSprite_current = self.player.PlayerSprite_down
            self.player.PlayerSprite_current.update()
            if not (self.walls[2].distanceTo(self.player.pos) < self.walls[2].thickness + self.player.radius + 1 and
                    self.walls[2].covers(self.player.pos)):
                self.player.vel.add(Vector(0, 1))
            else:
                self.player.vel = Vector(0, 0)

        if self.keyboard.right:
            self.player.PlayerSprite_current = self.player.PlayerSprite_right
            self.player.PlayerSprite_current.update()
            if not (self.walls[1].distanceTo(self.player.pos) < self.walls[1].thickness + self.player.radius + 1 and
                    self.walls[1].covers(self.player.pos)):
                self.player.vel.add(Vector(1, 0))
            else:
                self.player.vel = Vector(0, 0)

        if self.keyboard.left:
            self.player.PlayerSprite_current = self.player.PlayerSprite_left
            self.player.PlayerSprite_current.update()
            if not (self.walls[3].distanceTo(self.player.pos) < self.walls[3].thickness + self.player.radius + 1 and
                    self.walls[3].covers(self.player.pos)):
                self.player.vel.add(Vector(-1, 0))
            else:
                self.player.vel = Vector(0, 0)

    def shoot(self):
        if self.keyboard.arrow_up:
            # self.player.PlayerSprite_current = self.player.PlayerSprite_up
            # self.player.PlayerSprite_current.update()
            return self.player.shoot(Vector(0, -1).add(self.player.pos))

        if self.keyboard.arrow_down:
            # self.player.PlayerSprite_current = self.player.PlayerSprite_down
            # self.player.PlayerSprite_current.update()
            return self.player.shoot(Vector(0, 1).add(self.player.pos))

        if self.keyboard.arrow_right:
            # self.player.PlayerSprite_current = self.player.PlayerSprite_right
            # self.player.PlayerSprite_current.update()
            return self.player.shoot(Vector(1, 0).add(self.player.pos))

        if self.keyboard.arrow_left:
            # self.player.PlayerSprite_current = self.player.PlayerSprite_left
            # self.player.PlayerSprite_current.update()
            return self.player.shoot(Vector(-1, 0).add(self.player.pos))
