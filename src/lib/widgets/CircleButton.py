import pygame

from lib.widgets import Button


class CircleButton(Button):
    def __init__(self, screen, x, y, width, height, name=None, transparent=False):
        super().__init__(screen, x, y, width, height, name, transparent)

    def render(self):
        if self.name is not None:
            if not self.transparent:
                pygame.draw.circle(self.screen, (0, 0, 255), self.button.center, self.button.w / 2)
            self.screen.blit(self.text, self.button)
        else:
            if not self.transparent:
                pygame.draw.circle(self.screen, (0, 0, 255), self.button.center, self.button.w / 2)
