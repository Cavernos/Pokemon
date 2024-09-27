from app.Settings import Settings
from app.Settings.views import SettingsView

config = {
    Settings.__name__: Settings(),
    "views": {
        SettingsView.__name__: SettingsView
    }
}
