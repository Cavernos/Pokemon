import logging
from abc import abstractmethod

import pygame
import pyscroll
import pytmx

from lib import Container
from lib.events import EventListener, Event


class View:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def render(self):
        self.screen.fill((0, 0, 0))

    def __del__(self):
        for button in self.buttons:
            EventListener.remove_event_listener(pygame.MOUSEMOTION, button.on_hover)
            EventListener.remove_event_listener(pygame.MOUSEBUTTONDOWN, button.on_click)
        EventListener.remove_event_listener(pygame.KEYDOWN)
        EventListener.remove_event_listener(Event.TP)
        EventListener.remove_event_listener(Event.COLLIDE)
        EventListener.remove_event_listener(Event.KEY_PRESS)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)




class TiledView(View):
    def __init__(self, screen):
        super().__init__(screen)
        try:
            self.tmx_data = pytmx.load_pygame(f"{Container.get("ASSETS")}\\maps\\"
                                              f"{self.__class__.__name__.split('View')[0].lower()}.tmx")
        except FileNotFoundError as e:
            self.tmx_data = None
            logging.getLogger(__name__).warning(
                f"could not load : {self.__class__.__name__.split('View')[0].lower()}.tmx")

        if self.tmx_data is not None:
            map_data = pyscroll.data.TiledMapData(self.tmx_data)
            self.size = self.tmx_data.width * self.tmx_data.tilewidth, self.tmx_data.height * self.tmx_data.tileheight
            self.map_layer = pyscroll.BufferedRenderer(map_data, self.size)
            self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=6)

    def update(self):
        ...

    def render(self):
        if self.tmx_data is None:
            super().render()
        else:
            self.group.draw(self.screen)

    def __del__(self):
        super().__del__()
