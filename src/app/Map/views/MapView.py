from abc import ABC

import pygame.key

from app.Sprite import Sprite
from app.Sprite.entity import Player
from lib import Container
from lib.views import TiledView
from lib.widgets import Button


class MapView(TiledView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.map_layer.zoom = 5
        self.obstacles = []
        self.quit_menu = pygame.Surface((300, 100))
        self.accept_button = Button(screen, 100, 100, 30, 30, name='yes')
        self.discard_button = Button(screen, 10, 10, 100, 10, name='no')
        self.quit_visible = False
        for objs in self.tmx_data.objectgroups:
            for obj in objs:
                if objs.name == 'collision':
                    self.obstacles.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        if Container.exists(Sprite.__name__):
            self.player = Player(71 * 16, 84 * 16)
            self.player.obstacles = self.obstacles

    def update(self):
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        if self.quit_visible:
            self.screen.blit(self.quit_menu, (0, 0))
            self.accept_button.render()
        if Container.exists(Sprite.__name__):
            self.group.add(self.player)
        if True in pygame.key.get_pressed():
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, key=pygame.key.get_pressed()))
