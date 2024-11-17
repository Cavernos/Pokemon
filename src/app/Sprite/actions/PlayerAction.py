import pygame

from lib import Container
from lib.events import EventListener


class PlayerAction:
    def __call__(self, *args, **kwargs):
        self.player = args[0]
        EventListener.add_event_listener(pygame.USEREVENT, self.on_key_press)

    def on_key_press(self, event):
        if self.player.playable:
            for key, value in Container.get('inputs')['player'].items():
                if event.key[key] and hasattr(self.player, value):
                    self.player.update(Container.get('inputs')['player'][key])
                elif value == self.player.sprint.__name__:
                    self.player.slow()
