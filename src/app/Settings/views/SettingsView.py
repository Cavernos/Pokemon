from abc import ABC

from lib.views import View
from lib.widgets import Button


class SettingsView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.view_resize_button = Button(screen, 30, 30, 60, 60, "Resize")
        self.save_button = Button(screen, 30, 70, 60, 60, "save")

    def update(self):
        super().update()
        self.view_resize_button.render()
        self.save_button.render()