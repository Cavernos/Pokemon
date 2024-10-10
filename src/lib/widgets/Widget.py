class Widget:
    def __init__(self, screen, x, y, width, height, **kwargs):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def render(self):
        pass

    def set_style(self):
        pass
