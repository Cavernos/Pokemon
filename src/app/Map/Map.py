import os

from app.Map.actions import MapAction, HouseAction
from lib import Module


class Map(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        super().__init__()
        self.map_action = MapAction()
        self.house_action = HouseAction()
        self.pokemon_center_action = HouseAction()
