import pygame

from lib.events import EventListener
from lib.widgets.Label import Label
from lib.widgets.Widget import Widget


class Button(Widget):
    def __init__(self, screen, x, y, width, height, **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)
        self.name = kwargs.get('name')
        self.rect = pygame.Rect(x, y, width, height)
        if self.name is not None:
            self.text = Label(screen, x, y, width, height, name=self.name, font_weight="bold",
                              font_size=self.height // 2)
            self.button = self.text.get_rect()
            self.text.set_alpha(self.bg_color[3])
            self.button.topleft = self.rect.topleft
            self.button.w = self.rect.w
            self.button.h = self.rect.h
        else:
            self.button = self.rect
        self.image = pygame.Surface(self.button.size, pygame.SRCALPHA)
        self.image.fill(self.bg_color)
        self.is_hover = False
        self.action = None
        EventListener.add_event_listener(pygame.MOUSEMOTION, self.on_hover)
        EventListener.add_event_listener(pygame.MOUSEBUTTONDOWN, self.on_click)
        EventListener.add_event_listener(pygame.USEREVENT + 2, self.on_time_2)

    def render(self):
        print('render')
        if self.name is not None:
            if not self.transparent:
                self.screen.blit(self.image, self.button)
                self.text.render()
        else:
            if not self.transparent:
                self.screen.blit(self.image, self.button.topleft)

    def on_click(self, event):
        if self.action is not None and self.button.collidepoint(event.pos):
            self.fade_out(1000)
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

    def set_name(self, name):
        self.name = name
        self.text.set_name(name)

    def fade_in(self, millis):
        self.image.set_alpha(0)
        if self.name is not None:
            self.text.set_alpha(0)
        pygame.time.set_timer(pygame.USEREVENT + 1, millis // 255, loops=255)

    def fade_out(self, millis):
        #self.image.set_alpha(255)
        #if self.name is not None:
        #    self.text.set_alpha(255)
        pygame.time.set_timer(pygame.USEREVENT + 2, millis // 255, loops=255)
        # while self.image.get_alpha() != 0:
        #     self.set_alpha(self.image.get_alpha() - 1)
        #     pygame.time.delay(millis // 255)

    def set_alpha(self, value):
        self.image.set_alpha(value)
        if self.name is not None:
            self.text.set_alpha(value)

    def on_time(self, event):
        self.image.set_alpha(self.image.get_alpha() + 1)
        if self.name is not None:
            self.text.set_alpha(self.image.get_alpha() + 1)

    def on_time_2(self, event):
        print(self.image.get_alpha())
        self.set_alpha(self.image.get_alpha() - 1)
