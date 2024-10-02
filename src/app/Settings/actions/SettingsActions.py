import pygame

from lib import Container
from lib.views import ViewHandler


class SettingsActions:
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        self.view_handler.get_view().view_resize_button.set_action(self.resize)
        self.view_handler.get_view().save_button.set_action(self.save)

    def resize(self):
        if Container.exists("size"):
            Container.set("size", (1024, 1080))
            print(Container.get('size'))

    def save(self):
        pygame.display.set_mode(Container.get('size'))
