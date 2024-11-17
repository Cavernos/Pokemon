from abc import ABC

import pygame.key

from app.Sprite import Sprite
from app.Sprite.entity import Player, Pokemon
from lib import Container
from lib.loaders import LoaderInterface
from lib.views import TiledView
from lib.widgets import Button
from lib.widgets.Label import Label


class MapView(TiledView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.map_layer.zoom = 5
        self.obstacles = []
        self.quit_menu = pygame.Surface((300, 100))
        self.accept_button = Button(self.screen,
                                    self.quit_menu.get_rect(center=self.screen.get_rect().center).x,
                                    self.quit_menu.get_rect(center=self.screen.get_rect().center).y
                                    + self.quit_menu.get_height() - 30, 30, 30, name='yes')
        self.discard_button = Button(self.screen,
                                     self.quit_menu.get_rect(center=self.screen.get_rect().center).x
                                     + self.quit_menu.get_width() - 30,
                                     self.quit_menu.get_rect(center=self.screen.get_rect().center).y
                                     + self.quit_menu.get_height() - 30,
                                     30, 30, name='no')
        self.quit_label = Label(self.quit_menu, 0, self.quit_menu.get_height() / 2 - 20, 100, 20, name='Do you want to quit ?', color='#ffffff')
        self.quit_label.x = 1/2 * (self.quit_menu.get_width() - self.quit_label.get_rect().width)
        self.accept_button.set_alpha(0)
        self.discard_button.set_alpha(0)
        self.quit_visible = False
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
        if self.quit_visible:
            self.screen.blit(self.quit_menu, self.quit_menu.get_rect(center=self.screen.get_rect().center))
            self.accept_button.render()
            self.discard_button.render()
            self.quit_label.render()
        else:
            self.accept_button.set_alpha(0)
            self.discard_button.set_alpha(0)


