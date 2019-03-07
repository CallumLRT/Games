from vector import Vector

try:
    import simplegui
except ImportError:
    try:
        import simplegui2pygame as simplegui
    except ImportError:
        try:
            import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
        except ImportError:
            print("rip")
            exit()

import pygame


class Wheel:
    def __init__(self):
        self.IMG = simplegui.load_image('images/wheel.png')
        self.IMG_CENTRE = (256, 256)
        self.IMG_DIMS = (512, 512)
        self.vel = Vector(3, 0)
        self.STEP = 0
        self.imgRadius = 64
        self.IMG_Size = (128, 128)
        self.pos = Vector(CANVAS_DIMS[0] / 2, 2 * CANVAS_DIMS[1] / 3.)
        self.imgRot = 0

    def draw(self, canvas):
        if (self.pos.x < -self.imgRadius):
            self.pos.x = CANVAS_DIMS[0] + self.imgRadius
        if (self.pos.x <= (CANVAS_DIMS[0] + self.imgRadius)):

            self.imgRot += self.STEP
            canvas.draw_image(self.IMG, (256, 256), (512, 512), self.pos.get_p(), self.IMG_Size, self.imgRot)
        else:
            self.pos.x = -self.imgRadius

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.9)
        if (self.vel.x < -0.005):
            self.STEP = 0.5
        elif (self.vel.x > 0.005):
            self.STEP = -0.5
        else:
            self.STEP = 0


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.down = False
        self.up = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['down']:
            self.down = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False


class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
        if self.keyboard.down:
            self.wheel.vel.add(Vector(0, 1))
        if self.keyboard.up:
            self.wheel.vel.add(Vector(0, -1))


CANVAS_DIMS = (600, 400)

kbd = Keyboard()
wheel = Wheel()
inter = Interaction(wheel, kbd)


def draw(canvas):
    pygame.time.Clock().tick_busy_loop(60)
    inter.update()
    wheel.update()
    wheel.draw(canvas)


frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('white')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
