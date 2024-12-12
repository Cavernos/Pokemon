from abc import ABC

from app.Map.views import HouseView



class PokemonStoreView(HouseView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.player.set_pos((100, 96))