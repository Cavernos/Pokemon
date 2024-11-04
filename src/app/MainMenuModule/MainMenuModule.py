import os

from app.MainMenuModule.actions import MainMenuModuleAction
from lib import Module


class MainMenuModule(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        super().__init__()
        self.action = MainMenuModuleAction()
