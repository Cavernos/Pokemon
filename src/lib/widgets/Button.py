import pygame

from lib.events import EventListener


class Button:
    def __init__(self, screen, x, y, width, height, name=None, transparent=False):
        self.transparent = transparent
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name
        if name is not None:
            self.text = pygame.font.SysFont('Arial', self.rect.size[1] // 2).render(name, True, (255, 0, 255))
            self.button = self.text.get_rect()
            self.button.center = self.rect.center
        else:
            self.button = self.rect
        self.screen = screen
        self.is_hover = False
        self.action = None
        EventListener.add_event_listener(pygame.MOUSEMOTION, self.on_hover)
        EventListener.add_event_listener(pygame.MOUSEBUTTONDOWN, self.on_click)

    def render(self):
        if self.name is not None:
            if not self.transparent:
                pygame.draw.rect(self.screen, (0, 0, 255), self.button)
            self.screen.blit(self.text, self.button)
        else:
            if not self.transparent:
                pygame.draw.rect(self.screen, (0, 0, 255), self.rect)

    def on_click(self, event):
        if self.action is not None and self.button.collidepoint(event.pos):
            self.action(self)

    def on_hover(self, event):
        if self.button.collidepoint(event.pos) and not self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.is_hover = True
        if not self.button.collidepoint(event.pos) and self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.is_hover = False

    def set_action(self, action):
        self.action = action
