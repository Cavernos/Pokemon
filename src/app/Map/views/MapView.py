from abc import ABC

import pygame.key

from app.Sprite import Sprite
from app.Sprite.entity import Player
from lib import Container
from lib.views import TiledView


class MapView(TiledView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.map_layer.zoom = 5 / 2
        if Container.exists(Sprite.__name__):
            self.player = Player(71*16, 84*16)


    def update(self):
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        if hasattr(self, "player"):
            self.group.add(self.player)
        if True in pygame.key.get_pressed():
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, key=pygame.key.get_pressed()))
