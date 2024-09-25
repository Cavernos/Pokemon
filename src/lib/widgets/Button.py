import pygame

from lib.events import EventListener


class Button:
    def __init__(self, screen, x, y, width, height, name):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.text = pygame.font.SysFont('Arial', self.rect.size[1] // 2).render(name, True, (255, 0, 0))
        self.button = self.text.get_rect()
        self.button.center = self.rect.center
        self.screen = screen
        self.is_hover = False
        EventListener.add_event_listener(pygame.MOUSEMOTION, self.on_hover)

    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 0), self.button)
        self.screen.blit(self.text, self.button)

    def on_hover(self, event):
        if self.button.collidepoint(event.pos) and not self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.is_hover = True
        if not self.button.collidepoint(event.pos) and self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.is_hover = False
