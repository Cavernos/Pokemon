import pygame

from lib import Container
from lib.events import EventListener
from lib.views import ViewHandler, View


class ModuleActions:
    def __init__(self, view_handler=Container.get(ViewHandler.__name__)):
        self.view_handler = view_handler
        print(EventListener.listeners)

    @staticmethod
    @EventListener.add_event_listener(pygame.MOUSEBUTTONDOWN)
    def on_click(event):
        Container.get(ViewHandler.__name__).set_view(View)

