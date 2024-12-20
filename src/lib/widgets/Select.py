import pygame

from lib.widgets import Button
from lib.widgets.Widget import Widget


class Select(Widget):
    def __init__(self, screen, x, y, width, height, **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)
        self.name = kwargs.get('name') if "name" in kwargs.keys() else ""
        self.options = kwargs.get('options') if ('options' in kwargs.keys()
                                                 and isinstance(kwargs.get('options'), list)) else []
        self.options_button = [
            Button(screen, x, y + height * (i + 1), width, height, name=self.options[i]) for i
            in
            range(len(self.options))
        ]
        self.back_rect = pygame.Rect(x, y, width, height)
        self.selection_arrow = Button(screen, x + width, y, 20, height, bg_color=self.bg_color)
        self.selected_button = Button(screen, x, y, width, height, name=self.options[0])
        self.clicked = False
        self.is_hover = False
        self.selection_arrow.set_action(self.on_click)

    def render(self):
        pygame.draw.rect(self.screen, self.bg_color, self.back_rect)
        self.selection_arrow.render()
        for button in self.options_button:
            button.set_alpha(0)
        if self.clicked:
            for button in self.options_button:
                button.set_alpha(255)
                button.render()
        self.selected_button.render()

    def on_click(self, button):
        if not self.clicked:
            self.clicked = True
            self.back_rect.height = (self.back_rect.height * (len(self.options) + 1))
        else:
            self.back_rect.height = self.back_rect.height // (len(self.options) + 1)
            self.clicked = False

    def on_action(self, funct):
        for button in self.options_button:
            button.set_action(funct)
