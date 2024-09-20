from abc import abstractmethod

import pyscroll
import pytmx

from lib import Container


class View:
    def __init__(self, screen):
        self.screen = screen
        self.tmx_data = pytmx.load_pygame(f"{Container.get("APP")}\\assets\\maps\\{self.__class__.__name__.split('View')[0]}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)

    @abstractmethod
    def update(self): ...
