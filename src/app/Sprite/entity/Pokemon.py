import os

import pygame

from app.Sprite.entity import Entity
from lib import Container


class Pokemon(Entity):
    def __init__(self, x, y, index, width, height, texture, shiny_texture, *groups):
        super().__init__(x, y, width, height, *groups)
        self.index = index
        self.texture, self.shiny_texture = texture, shiny_texture
        self.loaded_image = pygame.image.load(os.path.join(Container.get('ASSETS'), 'entities', f'{index:03d}', self.texture))
        self.width = width // 2
        self.height = height // 4
        self.image = self.loaded_image.subsurface((0, 0, self.width, self.height))
        self.rect.size = self.width, self.height
        self.direction = 1

    def update(self, *args, **kwargs):
        if self.rect.x <= self.x + 25 and self.direction == 1:
            if self.rect.x >= self.x + 25:
                self.direction = 2
            self.move_right(1)
        if self.rect.y >= self.y - 25 and self.direction == 2:
            if self.rect.y <= self.y - 25:
                self.direction = 3
            self.move_up(1)
        if self.rect.x >= self.x and self.direction == 3:
            if self.rect.x <= self.x:
                self.direction = 4
            self.move_left(1)
        if self.rect.y <= self.y  and self.direction == 4:
            if self.rect.y >= self.y:
                self.direction = 1
            self.move_bottom(1)