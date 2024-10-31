import pygame

from lib import Container
from lib.events import EventListener
from lib.views import ViewHandler


class MapAction:
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        if hasattr(self.view_handler.get_view(), 'player'):
            self.player = self.view_handler.get_view().player
        EventListener.add_event_listener(pygame.KEYDOWN, self.on_key_press)

    def on_key_press(self, event):
        if Container.exists(event.key):
            getattr(self.player, Container.get('inputs')[event.key])(10)
