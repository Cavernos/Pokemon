from abc import ABC

import pygame.key

from app.Sprite import Sprite
from app.Sprite.entity import Player, Pokemon
from lib import Container
from lib.loaders import LoaderInterface
from lib.views import TiledView
from lib.widgets import Button, Menu
from lib.widgets.Label import Label


class MapView(TiledView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.map_layer.zoom = 5
        self.obstacles = []

        self.accept_button = Button(self.screen,0,70, 30, 30, name='yes')
        self.discard_button = Button(self.screen,270,70,30, 30, name='no')
        self.quit_label = Label(self.screen, 0, 100 / 2 - 20, 100, 20, name='Do you want to quit ?', color='#ffffff')
        self.quit_label.x = 1/2 * (300 - self.quit_label.get_rect().width)
        self.quit_menu = Menu(self.screen, self.screen.get_rect().centerx - 150, self.screen.get_rect().centery - 50, 300, 100, self.accept_button, self.discard_button, self.quit_label)
        self.quit_menu.set_alpha(0)
        self.hitbox_shown = False
        for objs in self.tmx_data.objectgroups:
            for obj in objs:
                if objs.name == 'collision':
                    self.obstacles.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        if Container.exists(Sprite.__name__):
            self.player = Player(71, 84)
            self.pokemon = Container.get(LoaderInterface.__name__).load_from_index(Pokemon, 1)
            self.player.obstacles = self.obstacles
            self.group.add(self.player)
            self.group.add(self.pokemon)
            self.entities = self.group.sprites()

    def update(self):
        if Container.exists(Sprite.__name__):
            #self.pokemon.update()
            if self.player.rect.colliderect(self.pokemon):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1, pos=(self.player.rect.x, self.player.rect.y)))
        if True in pygame.key.get_pressed():
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, key=pygame.key.get_pressed()))

    def render(self):
        if Container.exists(Sprite.__name__):
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
        else:
            self.map_layer.center((71 * 16, 84 * 16))
            self.map_layer.draw(self.screen, self.screen.get_rect())
        self.quit_menu.render()


