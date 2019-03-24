try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.down = False
        self.up = False
        self.arrow_right = False
        self.arrow_left = False
        self.arrow_down = False
        self.arrow_up = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        if key == simplegui.KEY_MAP["right"]:
            self.arrow_right = True
        if key == simplegui.KEY_MAP["left"]:
            self.arrow_left = True
        if key == simplegui.KEY_MAP["up"]:
            self.arrow_up = True
        if key == simplegui.KEY_MAP["down"]:
            self.arrow_down = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.right = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['w']:
            self.up = False
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        if key == simplegui.KEY_MAP["right"]:
            self.arrow_right = False
        if key == simplegui.KEY_MAP["left"]:
            self.arrow_left = False
        if key == simplegui.KEY_MAP["up"]:
            self.arrow_up = False
        if key == simplegui.KEY_MAP["down"]:
            self.arrow_down = False
