import pygame

from lib.widgets import Button


class Select:
    def __init__(self, screen, x, y, width, height, **kwargs):
        self.name = kwargs.get('name') if "name" in kwargs.keys() else ""
        self.options = kwargs.get('options') if ('options' in kwargs.keys()
                                                 and isinstance(kwargs.get('options'), list)) else []
        self.screen = screen
        self.options_button = [
            Button(screen, x, y + height * i, width, height, self.options[i]) for i in range(len(self.options))
        ]
        self.back_rect = pygame.Rect(x, y, width, height)
        self.selection_arrow = Button(screen, x + width, y, 20, height)
        self.clicked = False
        self.is_hover = False
        self.selection_arrow.set_action(self.on_click)

    def render(self):
        self.selection_arrow.render()
        pygame.draw.rect(self.screen, (0, 0, 255), self.back_rect)
        if self.clicked:
            for button in self.options_button:
                button.render()
        else:
            self.options_button[0].render()

    def on_click(self, button):
        if not self.clicked:
            self.clicked = True
            self.back_rect.height = (self.back_rect.height * len(self.options))
        else:
            self.back_rect.height = self.back_rect.height // len(self.options)
            self.clicked = False

    def on_action(self, funct):
        for button in self.options_button:
            button.set_action(funct)
