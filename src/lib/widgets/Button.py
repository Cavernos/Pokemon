import pygame

from lib.events import EventListener


class Button:
    def __init__(self, screen, x, y, width, height, name):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.text = pygame.font.SysFont('Arial', 45).render(name, True, (255, 0, 0))
        self.button = self.text.get_rect()
        self.button.center = self.rect.center
        self.screen = screen
        EventListener.add_event_listener(pygame.KEYDOWN, self.on_click)

    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 0), self.button)
        self.screen.blit(self.text, self.button)

    def on_click(self, event):
        if event.key == pygame.K_SPACE:
            print('click')
