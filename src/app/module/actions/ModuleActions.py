import pygame

from lib import Container
from lib.events import EventListener
from lib.views import ViewHandler, View


class ModuleActions:
    def __init__(self, view_handler=Container.get(ViewHandler.__name__)):
        self.view_handler = view_handler
        EventListener.remove_event_listener(pygame.MOUSEBUTTONDOWN, ModuleActions.on_click)
        print(EventListener.listeners)

    @staticmethod
    @EventListener.on(pygame.MOUSEBUTTONDOWN)
    def on_click(event):
        print(event)
        Container.get(ViewHandler.__name__).set_view(View)
        return

