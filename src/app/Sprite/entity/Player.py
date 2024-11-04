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
        self.rect.width = self.width
        self.rect.height = self.height
        self.feet = pygame.Rect(self.rect.x, self.rect.height + 12, self.width * 0.5, 12)

    def move(self, func_name):
        old_position = [self.rect.x, self.rect.y].copy()
        getattr(self, func_name)(1)
        self.position = [self.rect.x, self.rect.y].copy()
        self.feet.midbottom = self.rect.midbottom
        if self.feet.collidelist(self.obstacles) != -1:
            self.position = old_position
            self.rect.topleft = old_position
            self.feet.midbottom = self.rect.midbottom

