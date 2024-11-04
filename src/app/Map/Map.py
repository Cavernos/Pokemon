import os

from app.Map.actions import MapAction
from lib import Module


class Map(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        self.action = MapAction()
