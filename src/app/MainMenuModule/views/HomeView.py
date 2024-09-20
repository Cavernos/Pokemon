from abc import ABC

import pygame.display

from lib.views import View


class HomeView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        self.group.draw(self.screen)
        pygame.display.flip()
