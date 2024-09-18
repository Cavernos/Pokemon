import pygame

from lib.views import View


class HomeView(View):
    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255)

    def update(self):
        pygame.display.get_surface().fill(self.color)
        pygame.display.flip()
