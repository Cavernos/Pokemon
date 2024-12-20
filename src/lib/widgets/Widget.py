import pygame


class Widget:
    def __init__(self, screen, x, y, width, height, **kwargs):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.transparent = kwargs.get('transparent') if kwargs.get('transparent') is not None else False
        self.bg_color = pygame.Color(kwargs.get('bg_color')) if kwargs.get('bg_color') is not None else (255, 255, 255, 255)
        self.color = pygame.Color(kwargs.get('color')) if kwargs.get('color') is not None else (0, 0, 0, 255)
        self.animation = None


    def get_pos(self):
        return self.x, self.y

    def set_pos(self, value):
        self.x, self.y = value

    def render(self):
        ...

    def set_animation(self, animation):
        self.animation = animation

    def set_alpha(self, integer):
        ...
