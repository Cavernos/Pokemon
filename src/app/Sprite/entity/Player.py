import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))

    def move_left(self, x):
        self.rect.x -= x

    def move_right(self, x):
        self.rect.x += x

    def move_bottom(self, y):
        self.rect.y += y

    def move_up(self, y):
        self.rect.y -= y
