import pygame

from lib.widgets import Button


class CircleButton(Button):
    def __init__(self, screen, x, y, width, height,  **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)

    def render(self):
        if self.name is not None:
            if not self.transparent:
                pygame.draw.circle(self.screen, self.bg_color, self.button.center, self.button.w / 2)
            self.screen.blit(self.text, self.button)
        else:
            if not self.transparent:
                pygame.draw.circle(self.screen, self.bg_color, self.button.center, self.button.w / 2)
