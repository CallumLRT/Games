try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

WIDTH = 500
HEIGHT = 500
a = 0
b = 0


def randCol():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'


# Drawing handler:
# this function is called 60 times per second
def draw(canvas):
    global a
    global b
    if (a % 60 == 0):
        canvas.draw_circle((WIDTH / 2, HEIGHT / 2), 20, 40, 'green', 'white')
        canvas.draw_circle((240, 240), 20, 40, 'white', 'white')
        a = a + 1
    else:
        canvas.draw_circle((WIDTH / 2, HEIGHT / 2), 20, 40, 'red', 'white')
        canvas.draw_circle((240, 240), 20, 40, 'blue', 'white')
        a = a + 1
    b = b + 1


# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Colours", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
