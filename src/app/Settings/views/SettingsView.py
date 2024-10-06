from abc import ABC

from lib.views import View
from lib.widgets import Button
from lib.widgets import Select


class SettingsView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.view_resize_button = Button(screen, 30, 30, 60, 60, "Resize")
        self.save_button = Button(screen, 30, 70, 60, 60, "save")
        self.select = Select(screen, 200, 65, 75, 30, name="Hello",
                             options=["1024x1080", '1920x1080', '960x640'])

    def update(self):
        super().update()
        self.view_resize_button.render()
        self.save_button.render()
        self.select.render()
