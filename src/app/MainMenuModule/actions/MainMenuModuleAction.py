from app.Map import Map
from app.Map.views import MapView
from app.Settings import Settings
from app.Settings.views import SettingsView
from lib import Container
from lib.views import ViewHandler


class MainMenuModuleAction:
    def __call__(self):
        self.view_handler = Container.get(ViewHandler.__name__)
        self.buttons = self.view_handler.get_view().buttons
        self.buttons[0].set_action(self.go_to_settings)
        self.buttons[1].set_action(self.play)

    def go_to_settings(self, button):
        if Container.exists(Settings.__name__):
            self.view_handler.set_view(Container.get(SettingsView.__name__))

    def play(self, button):
        if Container.exists(Map.__name__):
            self.view_handler.set_view(Container.get(MapView.__name__))
