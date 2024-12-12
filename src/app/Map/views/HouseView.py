from abc import ABC

import pygame

from app.Sprite import Sprite
from app.Sprite.entity import Player
from lib import Container
from lib.events import Event
from lib.views import TiledView
from lib.widgets import Menu, Button
from lib.widgets.Label import Label


class HouseView(TiledView, ABC):

    def __init__(self, screen):
            super().__init__(screen)
            self.map_layer.zoom = 0.5
            self.objects = {}

            self.accept_button = Button(self.screen, 0, 70, 30, 30, name='yes')
            self.discard_button = Button(self.screen, 270, 70, 30, 30, name='no')
            self.quit_label = Label(self.screen, 0, 100 / 2 - 20, 100, 20, name='Do you want to quit ?',
                                    color='#ffffff')
            self.quit_label.x = 1 / 2 * (300 - self.quit_label.get_rect().width)
            self.quit_menu = Menu(self.screen, self.screen.get_rect().centerx - 150,
                                  self.screen.get_rect().centery - 50, 300, 100, self.accept_button,
                                  self.discard_button, self.quit_label)
            self.quit_menu.set_alpha(0)
            self.hitbox_shown = False

            for objs in self.tmx_data.objectgroups:
                self.objects[objs.name] = []
                for obj in objs:
                    self.objects[objs.name].append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            if Container.exists(Sprite.__name__):
                self.player = Container.get('player') if Container.get('player') is not None else Player(144, 128)
                self.old_player_pos = (self.player.rect.x, self.player.rect.y + 1)
                Container.delete('player')
                self.player.set_pos((148, 128))
                self.player.obstacles = self.objects['collision']
                self.group.add(self.player)

    def update(self):
        if Container.exists(Sprite.__name__):
            if self.player.rect.collidelist(self.objects['tp']) != -1:
                pygame.event.post(pygame.event.Event(Event.TP, pos=self.old_player_pos))
        if True in pygame.key.get_pressed():
            pygame.event.post(pygame.event.Event(Event.KEY_PRESS, key=pygame.key.get_pressed()))



    def render(self):
        if Container.exists(Sprite.__name__):
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            if self.player.inventory_shown:
                self.player.show_inventory()
            else:
                self.player.inventory_menu.set_alpha(0)
        else:
            self.map_layer.center((9* 16, 8 * 16))
            self.map_layer.draw(self.screen, self.screen.get_rect())
        self.quit_menu.render()


