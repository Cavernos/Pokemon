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
        self.animation_counter = [0 for i in range(4)]
        self.velocity = 1
        
        # collision
        self.position = [x, y]
        self.feet = pygame.Rect(self.rect.x + self.width * 0.5, self.rect.height + 12, self.width * 0.5, 12)
        self.obstacles = []
        
    # movements
    def move_left(self, x):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(0)*self.width, self.height, self.width, self.height))
        self.rect.x -= (x * self.velocity)
        self.feet.x -= (x * self.velocity)

    def move_right(self, x):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(1) * self.width, 2*self.height, self.width, self.height))
        self.rect.x += (x * self.velocity)
        self.feet.x += (x * self.velocity)

    def move_bottom(self, y):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(2) * self.width, 0 * self.height, self.width, self.height))
        self.rect.y += (y * self.velocity)
        self.feet.y += (y * self.velocity)

    def move_up(self, y):
        self.image = self.loaded_image.subsurface(
            (self.play_anim(3) * self.width, 3 * self.height, self.width, self.height))
        self.rect.y -= (y * self.velocity)
        self.feet.y -= (y * self.velocity)
        
    def move(self, func_name):
        print('moving')
        old_position = [self.rect.x, self.rect.y].copy()
        getattr(self, func_name)(1)
        self.position = [self.rect.x, self.rect.y].copy()
        
        print(self.feet)
        
        if self.feet.collidelist(self.obstacles) != -1:
            print('COLLISION')
            self.position = old_position
            self.rect.topleft = old_position
            self.feet.midbottom = self.rect.midbottom

    def sprint(self, multiplier):
        self.velocity = 2

    def slow(self):
        self.velocity = 1

    def play_anim(self, counter_index):
        self.animation_counter[counter_index] += (self.velocity / 2)
        if self.animation_counter[counter_index] >= 4:
            self.animation_counter[counter_index] = 0
        return int(self.animation_counter[counter_index])

