import pygame

from lib.events import EventListener
from lib.widgets.Widget import Widget


class Button(Widget):
    def __init__(self, screen, x, y, width, height, **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)
        self.name = kwargs.get('name')
        self.rect = pygame.Rect(x, y, width, height)
        if self.name is not None:
            self.text = pygame.font.SysFont('Arial', self.height // 2, bold=True).render(self.name, True, self.color)
            self.button = self.text.get_rect()
            self.text.set_alpha(self.bg_color[3])
            self.button.topleft = self.rect.topleft
            self.button.h = self.rect.h
        else:
            self.button = self.rect
        self.image = pygame.Surface(self.button.size, pygame.SRCALPHA)

        self.image.fill(self.bg_color)
        self.is_hover = False
        self.action = None
        EventListener.add_event_listener(pygame.MOUSEMOTION, self.on_hover)
        EventListener.add_event_listener(pygame.MOUSEBUTTONDOWN, self.on_click)
        EventListener.add_event_listener(pygame.USEREVENT, self.on_time)
        self.fade_in(1000)

    def render(self):
        if self.name is not None:
            if not self.transparent:
                self.text = pygame.font.SysFont('Arial', self.height // 2, bold=True).render(self.name, True,
                                                                                             self.color)
                self.screen.blit(self.image, self.button)
                self.screen.blit(
                    self.text, self.button)
        else:
            if not self.transparent:
                self.screen.blit(self.image, self.button.topleft)

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

    def fade_in(self, millis):
        self.image.set_alpha(0)
        if self.name is not None:
            self.text.set_alpha(0)
        pygame.time.set_timer(pygame.USEREVENT, millis // 255, loops=millis % 255)

    def on_time(self, event):
        self.image.set_alpha(self.image.get_alpha() + 1)
        if self.name is not None:
            self.text.set_alpha(self.image.get_alpha() + 1)
