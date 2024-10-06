from app.Settings.views import SettingsView
from lib import Container
from lib.views import ViewHandler


class MainMenuModuleAction:
    def __call__(self):
        self.view_handler = Container.get(ViewHandler.__name__)
        self.buttons = self.view_handler.get_view().buttons
        self.buttons[0].set_action(self.go_to_settings)

    def go_to_settings(self, button):
        self.view_handler.set_view(Container.get(SettingsView.__name__))
