import pygame

from lib.views import View


class HomView(View):
    def __init__(self, screen):
        super().__init__(screen)
        self.color = (255, 255, 255)

    def update(self):
        pygame.display.get_surface().fill(self.color)
        pygame.display.flip()
