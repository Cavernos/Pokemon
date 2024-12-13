import os.path

from app.Settings.actions import SettingsActions
from lib import Module


class Settings(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        super().__init__()
        self.settings_action = SettingsActions()
