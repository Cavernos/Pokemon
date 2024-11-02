import pygame

from lib import Container
from lib.events import EventListener


class PlayerAction:
    def __call__(self, *args, **kwargs):
        self.player = args[0]
        EventListener.add_event_listener(pygame.USEREVENT, self.on_key_press)

    def on_key_press(self, event):
        for key, value in Container.get('inputs').items():
            if event.key[key]:
                getattr(self.player, Container.get('inputs')[key])(1)
            elif value == self.player.sprint.__name__:
                    self.player.slow()
