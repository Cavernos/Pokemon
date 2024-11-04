import os

import pygame

from app.Sprite.entity import Entity
from lib import Container


class Player(Entity):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, name='player', *groups)
        self.loaded_image = pygame.image.load(os.path.join(Container.get('ASSETS'), 'entities', 'player.png'))
        self.width = self.width // 4
        self.height = self.height // 4
        self.image = self.loaded_image.subsurface((0, 0, self.width, self.height))

