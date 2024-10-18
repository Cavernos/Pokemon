import pygame.font

from lib.widgets.Widget import Widget


class Label(Widget):
    def __init__(self, screen, x, y, width, height, **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)
        self.name = kwargs.get('name')
        self.font_size = kwargs.get('font_size') if kwargs.get('font_size') is not None else self.height
        self.font_weight = kwargs.get('font_weight') if kwargs.get('font_weight') is not None else "regular"
        self.font_name = kwargs.get('font_name') if kwargs.get('font_name') is not None else "Arial"
        if self.name is not None:
            match self.font_weight.lower().strip():
                case "bold":
                    self.text = pygame.font.SysFont(self.font_name, self.font_size, True)
                case "italic":
                    self.text = pygame.font.SysFont(self.font_name, self.font_size, False, True)
                case _:
                    self.text = pygame.font.SysFont(self.font_name, self.font_size, False, False)
        self.text_surface = self.text.render(self.name, True, self.color)

    def render(self):
        if self.name is not None:
            self.screen.blit(self.text_surface, (self.x, self.y))

    def set_alpha(self, new_alpha):
        self.text_surface.set_alpha(new_alpha)

    def set_name(self, name):
        self.name = name
        self.text_surface = self.text.render(self.name, True, self.color)

    def get_rect(self):
        return self.text_surface.get_rect()