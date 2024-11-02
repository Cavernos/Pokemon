import pygame
from Sprite import Entity
from keylistener import KeyListener
from screen import Screen

class Player(Entity):
    def __init__(self, *groups, keylistener = KeyListener, screen = Screen, x : int, y : int):
        super().__init__(*groups,keylistener,screen, x, y)
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
    
    def update(self):
        self.move()
        self.check_move()
        super().update()
    
    def check_move(self):
        if self.animation_walk is False : 
            
            if self.keylistener.key_pressed(pygame.K_q):
                self.move_left()
            elif self.keylistener.key_pressed(pygame.K_d):
                self.move_right()
            elif self.keylistener.key_pressed(pygame.K_z):
                self.move_up()
            elif self.keylistener.key_pressed(pygame.K_s):
                self.move_down()
