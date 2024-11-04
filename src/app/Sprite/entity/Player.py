import os

import pygame

from lib import Container


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.loaded_image = pygame.image.load(os.path.join(Container.get('APP'), 'assets', 'character', 'player.png'))
        self.width = self.loaded_image.get_width() // 4
        self.height = self.loaded_image.get_height() // 4
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = self.loaded_image.subsurface((4, 6, self.width, self.height))
        self.velocity = 1

    def move_left(self, x):
        self.image = self.loaded_image.subsurface((0, self.height, self.width, self.height))
        self.rect.x -= (x * self.velocity)

    def move_right(self, x):
        self.image = self.loaded_image.subsurface((0, 2*self.height, self.width, self.height))
        self.rect.x += (x * self.velocity)

    def move_bottom(self, y):
        self.image = self.loaded_image.subsurface((0, 0, self.width, self.height))
        self.rect.y += (y * self.velocity)

    def move_up(self, y):
        self.image = self.loaded_image.subsurface((0, 3*self.height, self.width, self.height))
        self.rect.y -= (y * self.velocity)

    def sprint(self, multiplier):
        self.velocity = 2

    def slow(self):
        self.velocity = 1
