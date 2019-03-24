class Button:
    def __init__(self, pos, image, image_center, image_size, action):
        self.pos = pos
        self.image = image
        self.image_center = image_center
        self.image_size = image_size
        self.action = action
        self.selected = False

    def __str__(self):
        a = "BUTTON:" + "\n"
        a += "Position: " + str(self.pos) + "\n"
        a += "Image: " + str(self.image) + "\n"
        a += "Action: " + str(self.action) + "\n"
        a += "Selected: " + str(self.selected) + "\n"
        a += "\n"
        return a

    def draw(self, canvas):
        if not self.selected:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size)
        else:
            canvas.draw_image(self.image, [self.image_center[0], self.image_center[1] + self.image_size[1]],
                              self.image_size, self.pos, self.image_size)

    def activate(self):
        self.action()

    def in_button(self, pos):
        if pos[0] < self.pos[0] + self.image_size[0] / 2 and pos[0] > self.pos[0] - self.image_size[0] / 2:
            if pos[1] < self.pos[1] + self.image_size[1] / 2 and pos[1] > self.pos[1] - self.image_size[1] / 2:
                return True
        return False

    def get_pos(self):
        return self.pos

    def set_pos(self, p):
        self.pos = p

    def get_image(self):
        return self.image

    def get_image_center(self):
        return self.image_center

    def get_image_size(self):
        return self.image_size

    def set_image(self, i, c, s):
        self.image = i
        self.image_center = c
        self.image_size = s

    def get_action(self):
        return self.action

    def set_action(self, a):
        self.action = a

    def get_selected(self):
        return self.selected

    def set_selected(self, s):
        self.selected = s

    def switch_selected(self):
        self.selected = not self.selected
        return self.selected


