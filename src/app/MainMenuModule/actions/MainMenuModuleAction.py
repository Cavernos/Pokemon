import pygame

from app.Settings.views import SettingsView
from lib import Container
from lib.events import EventListener
from lib.views import ViewHandler


class MainMenuModuleAction:
    def __init__(self):
        self.view_handler = Container.get(ViewHandler.__name__)
        EventListener.add_event_listener(pygame.MOUSEBUTTONDOWN, self.on_click)

    def on_click(self, event):
        for button in self.view_handler.get_view().buttons:
            if button.name == "Settings" and button.rect.collidepoint(event.pos) and Container.exists(SettingsView.__name__):
                self.view_handler.set_view(Container.get(SettingsView.__name__))
                return


