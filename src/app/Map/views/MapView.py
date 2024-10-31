from abc import ABC

from app.Sprite import Sprite
from app.Sprite.entity import Player
from lib import Container
from lib.views import View


class MapView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        if Container.exists(Sprite.__name__):
            self.player = Player()

    def update(self):
        super().update()
        if hasattr(self, "player"):
            self.player.render()
