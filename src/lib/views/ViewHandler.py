import re

import pygame.display

from lib import Container


class ViewHandler:
    def __init__(self):
        self.curent_view = None

    def set_view(self, view):
        del self.curent_view
        if pygame.display.get_init():
            if Container.exists(view.__name__):
                self.curent_view = view(pygame.display.get_surface())
                attr_name = f'{'_'.join(re.findall('.[^A-Z]*', view.__name__)[:-1]).lower()}_action'
                if hasattr(Container.get(view.__module__.split('.')[1]), attr_name):
                    if callable(getattr(Container.get(view.__module__.split('.')[1]), attr_name)):
                        getattr(Container.get(view.__module__.split('.')[1]), attr_name)()
            else:
                self.curent_view = None

    def update(self):
        if self.curent_view is not None:
            self.curent_view.update()

    def render(self):
        if self.curent_view is not None:
            self.curent_view.render()

    def get_view(self):
        return self.curent_view
