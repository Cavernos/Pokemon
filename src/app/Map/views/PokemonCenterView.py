from abc import ABC

import pygame

from app.Map.views import HouseView
from app.Sprite import Sprite
from lib import Container
from lib.views import TiledView
from lib.widgets import Button, Menu
from lib.widgets.Label import Label


class PokemonCenterView(HouseView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.player.set_pos((116, 128))