import os

import pygame.sprite

from lib import Container


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, *groups):
        super().__init__(*groups)

        self.number_of_sprite = 2
        self.x = x * 16
        self.y = y * 16
        self.loaded_image = pygame.Surface((width, height))
        self.width = self.loaded_image.get_width()
        self.height = self.loaded_image.get_height()
        self.image = self.loaded_image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.animation_counter = [0 for i in range(4)]
        self.position = [x, y]
        self.obstacles = []
        self.playable = False
        self.velocity = 1

    def move_left(self, x):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(0) * self.width, self.height, self.width, self.height)
        )
        self.rect.x -= (x * self.velocity)

    def move_right(self, x):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(1) * self.width, 2 * self.height, self.width, self.height))
        self.rect.x += (x * self.velocity)

    def move_bottom(self, y):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(2) * self.width, 0 * self.height, self.width, self.height))
        self.rect.y += (y * self.velocity)

    def move_up(self, y):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(3) * self.width, 3 * self.height, self.width, self.height))
        self.rect.y -= (y * self.velocity)

    def sprint(self, multiplier):
        self.velocity = 2

    def slow(self):
        self.velocity = 1

    def play_anim(self, counter_index):
        self.animation_counter[counter_index] += (self.velocity / 10)
        if self.animation_counter[counter_index] >= self.number_of_sprite:
            self.animation_counter[counter_index] = 0
        return int(self.animation_counter[counter_index])

    def show_hitbox(self):
        pygame.draw.rect(self.image, (0, 0, 0),
                                     (0,0,
                                      self.rect.width, self.rect.height), width=1)



