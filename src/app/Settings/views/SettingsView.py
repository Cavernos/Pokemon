from abc import ABC

from lib.views import View


class SettingsView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        super().update()