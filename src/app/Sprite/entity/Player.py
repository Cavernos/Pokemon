import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.rect = pygame.Rect(0, 0, 45,45)

    def move_left(self, x):
        self.rect.x += x

    def move_right(self, x):
        self.rect.x -= x

    def move_bottom(self, y):
        self.rect.y += y

    def move_up(self, y):
        self.rect.y -= y
    def render(self):
        pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), self.rect)