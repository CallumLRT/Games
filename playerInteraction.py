try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector


class PlayerInteraction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
            self.wheel.PlayerSprite_current = self.wheel.PlayerSprite_right

        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
            self.wheel.PlayerSprite_current = self.wheel.PlayerSprite_left

        if self.keyboard.down:
            self.wheel.vel.add(Vector(0, 1))
            self.wheel.PlayerSprite_current = self.wheel.PlayerSprite_down

        if self.keyboard.up:
            self.wheel.vel.add(Vector(0, -1))
            self.wheel.PlayerSprite_current = self.wheel.PlayerSprite_up
