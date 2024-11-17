import os

import pygame

from app.Sprite.entity import Entity
from lib import Container


class Player(Entity):
    def __init__(self, x, y, width=100, height=128, *groups):
        super().__init__(x, y, width, height, *groups)
        self.loaded_image = pygame.image.load(os.path.join(Container.get('ASSETS'), 'entities', 'player.png'))
        self.number_of_sprite = 4
        self.width = self.loaded_image.get_width() // 4
        self.height = (self.loaded_image.get_height() // 4)
        self.image = self.loaded_image.subsurface((0, 0, self.width, self.height))
        self.rect.size = self.width, self.height
        self.playable = True
        self.feet = pygame.Rect(self.x, self.y, self.width - 10, self.height * 0.5)

    def update(self, *args, **kwargs):
        func_name = args[0]
        old_position = [self.rect.x, self.rect.y].copy()
        if hasattr(self, func_name):
            getattr(self, func_name)(1)
        self.position = [self.rect.x, self.rect.y].copy()
        self.feet.midbottom = self.rect.midbottom
        if self.feet.collidelist(self.obstacles) != -1:
            self.position = old_position
            self.rect.topleft = old_position
            self.feet.midbottom = self.rect.midbottom

