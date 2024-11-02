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
        self.velocity = 1

    def move_left(self, x):
        self.rect.x -= (x * self.velocity)

    def move_right(self, x):
        self.rect.x += (x * self.velocity)

    def move_bottom(self, y):
        self.rect.y += (y * self.velocity)

    def move_up(self, y):
        self.rect.y -= (y * self.velocity)

    def sprint(self, multiplier):
        self.velocity = 2

    def slow(self):
        self.velocity = 1
