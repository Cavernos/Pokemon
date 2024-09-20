from abc import ABC

import pygame.display

from lib.views import View
from lib.widgets import Button


class HomeView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.button = Button(self.screen, 120, 60, 200, 200, "hello")

    def update(self):
        self.group.draw(self.screen)
        self.button.render()
        pygame.display.update()
