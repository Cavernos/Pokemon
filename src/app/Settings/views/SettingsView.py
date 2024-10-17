from abc import ABC

from app.Settings.views import DisplayTable, InputsTab
from lib.views import View
from lib.widgets.TableLayout import TableLayout


class SettingsView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.display_table = TableLayout(
            screen, 160, 10, 600, 500,
            tables={'DisplayTable': DisplayTable, 'hello': InputsTab})

    def update(self):
        super().update()
        self.display_table.render()
