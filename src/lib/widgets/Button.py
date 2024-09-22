import pygame

from lib.events import EventListener


class Button:
    def __init__(self, screen, x, y, width, height, name):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        print(self.rect.size)
        self.text = pygame.font.SysFont('Arial', self.rect.size[1]//2).render(name, True, (255, 0, 0))
        self.button = self.text.get_rect()
        self.button.center = self.rect.center
        self.screen = screen
        EventListener.add_event_listener(pygame.MOUSEBUTTONDOWN, self.on_click)
        EventListener.add_event_listener(pygame.MOUSEMOTION, self.on_hover)

    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 0), self.button)
        self.screen.blit(self.text, self.button)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            print('click')

    def on_hover(self, event):
        if self.rect.collidepoint(event.pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)





