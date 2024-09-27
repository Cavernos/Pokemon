import pygame.display


class ViewHandler:
    def __init__(self):
        self.curent_view = None

    def set_view(self, view):
        try:
            if pygame.display.get_init():
                try:
                    self.curent_view = view(pygame.display.get_surface())
                except AttributeError as e:
                    self.curent_view = None

        except NameError as e:
            return e

    def update(self):
        if self.curent_view is not None:
            self.curent_view.update()
        else:
            pygame.display.get_surface().fill((0, 0, 0))

    def get_view(self):
        return self.curent_view
