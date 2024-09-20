import pygame.display


class ViewHandler:
    def __init__(self):
        self.curent_view = None

    def set_view(self, view):
        self.curent_view = view(pygame.display.get_surface())

    def update(self):
        if self.curent_view is not None:
            self.curent_view.update()
        else:
            pygame.display.get_surface().fill((0, 0, 0))

    def get_view(self):
        return self.curent_view
