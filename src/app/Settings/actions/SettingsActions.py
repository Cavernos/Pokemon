import pygame

from lib import Container
from lib.views import ViewHandler


class SettingsActions:
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        #self.view_handler.get_view().view_resize_button.set_action(self.resize)
        self.view_handler.get_view().save_button.set_action(self.save)
        self.view_handler.get_view().select.on_action(self.resize)

    def resize(self, option):
        self.view_handler.get_view().select.on_click(option)
        self.view_handler.get_view().select.selected_button.name = option.name
        if Container.exists("size"):
            Container.set("size", tuple(int(i) for i in option.name.split('x')))
            print(Container.get('size'))

    def save(self, button):
        pygame.display.set_mode(Container.get('size'))
