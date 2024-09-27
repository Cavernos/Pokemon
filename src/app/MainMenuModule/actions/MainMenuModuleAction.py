import pygame

from lib import Container
from lib.events import EventListener
from lib.views import ViewHandler


class MainMenuModuleAction:
    def __init__(self):
        self.view = Container.get(ViewHandler.__name__).get_view()
        EventListener.add_event_listener(pygame.MOUSEBUTTONDOWN, self.settings_action)

    def settings_action(self, event):
        print(self.view)
        print(event.pos)


