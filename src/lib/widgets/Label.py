import pygame.font

from lib.widgets.Widget import Widget


class Label(Widget):
    def __init__(self, screen, x, y, width, height, **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)
        self.name = kwargs.get('name')
        self.font_size = kwargs.get('font_size') if kwargs.get('font_size') is not None else self.height
        self.font_weight = kwargs.get('font_weight') if kwargs.get('font_weight') is not None else "regular"
        self.font_name = kwargs.get('font_name') if kwargs.get('font_name') is not None else "Arial"
        self.text_surfaces = []
        if self.name is not None:
            match self.font_weight.lower().strip():
                case "bold":
                    self.text = pygame.font.SysFont(self.font_name, self.font_size, True)
                case "italic":
                    self.text = pygame.font.SysFont(self.font_name, self.font_size, False, True)
                case _:
                    self.text = pygame.font.SysFont(self.font_name, self.font_size, False, False)
            for line in self.name.splitlines():
                self.text_surfaces.insert(self.name.splitlines().index(line), self.text.render(line, True, self.color))

    def render(self):
        if self.name is not None:
            for surface in self.text_surfaces:
                self.screen.blit(surface, (self.x, self.y + self.height*self.text_surfaces.index(surface)))

    def set_alpha(self, new_alpha):
        for surface in self.text_surfaces:
            surface.set_alpha(new_alpha)

    def set_name(self, name):
        self.text_surfaces = []
        self.name = name
        for line in self.name.splitlines():
            self.text_surfaces.insert(self.name.splitlines().index(line), self.text.render(line, True, self.color))

    def get_rect(self, **kwargs):
        return pygame.Rect(
            self.text_surfaces[0].get_rect(**kwargs).x,
            self.text_surfaces[-1].get_rect(**kwargs).y + len(self.text_surfaces)*self.height,
            self.text_surfaces[0].get_rect(**kwargs).width,
            self.text_surfaces[0].get_rect(**kwargs).height
        )
