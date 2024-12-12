import pygame

from lib import Container
from lib.events import EventListener, Event


class PlayerAction:
    def __call__(self, *args, **kwargs):
        """
        Appelé lorsque l'instance est appelé
        Args:
            *args: tuple
            **kwargs: dict

        Returns:

        """
        self.player = args[0]
        EventListener.add_event_listener(Event.KEY_PRESS, self.on_key_press)
        EventListener.add_event_listener(pygame.KEYDOWN, self.on_key_down)

    def on_key_press(self, event):
        """
        Est joué  lorsque l'on presse une touche
        Args:
            event:

        Returns:

        """
        if self.player.playable:
            for key, value in Container.get('inputs')['player'].items():
                if event.key[key] and hasattr(self.player, value):
                    if value == self.player.show_inventory.__name__:
                        return
                    else:
                        self.player.update(Container.get('inputs')['player'][key])
                elif value == self.player.sprint.__name__:
                    self.player.slow()

    def on_key_down(self, event):
        for key, value in Container.get('inputs')['player'].items():
            if value == self.player.show_inventory.__name__ and event.key == key:
                if self.player.inventory_shown:
                    self.player.inventory_shown = False
                    return
                self.player.inventory_shown = True
