import random
from abc import ABC

import pygame

from app.Map.animations import TutorialScene
from app.Sprite import Sprite
from app.Sprite.entity import Player, Pokemon
from lib import Container
from lib.events import Event
from lib.loaders import LoaderInterface
from lib.views import TiledView
from lib.widgets import Button, Menu
from lib.widgets.Label import Label


class MapView(TiledView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.map_layer.zoom = 5
        self.objects = {}

        self.accept_button = Button(self.screen,0,70, 30, 30, name='yes')
        self.discard_button = Button(self.screen,270,70,30, 30, name='no')
        self.quit_label = Label(self.screen, 0, 100 / 2 - 20, 100, 20, name='Do you want to quit ?', color='#ffffff')
        self.quit_label.x = 1/2 * (300 - self.quit_label.get_rect().width)
        self.quit_menu = Menu(self.screen, self.screen.get_rect().centerx - 150, self.screen.get_rect().centery - 50, 300, 100, self.accept_button, self.discard_button, self.quit_label)
        self.quit_menu.set_alpha(0)
        self.hitbox_shown = False

        for objs in self.tmx_data.objectgroups:
            self.objects[objs.name] = []
            if objs.name == 'tp':
                self.objects[objs.name] = {}

            for obj in objs:
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                if objs.name == 'tp':
                    self.objects[objs.name][obj.name] = rect
                else:
                    self.objects[objs.name].append(rect)

        if Container.exists(Sprite.__name__):
            self.player = Container.get('player') if isinstance(Container.get('player'), Player) else Player(71, 84)
            Container.delete('player')
            if Container.get('pokemon') is not None:
                self.pokemons = Container.get('pokemon')
            else:
                self.pokemons = []
                self.generate_pokemon()
            self.player.obstacles = self.objects['collision']
            self.group.add(self.player)
            self.entities = self.group.sprites()
            self.tutorial = TutorialScene(self.player, random.sample(self.pokemons, 1)[0])

    def update(self):
        if Container.exists(Sprite.__name__):
            for pokemon in self.pokemons:
                pokemon.update()
            if self.player.rect.collidelist(self.pokemons) != -1:
                pygame.event.post(pygame.event.Event(Event.COLLIDE,
                                                     pos=(self.player.rect.x, self.player.rect.y)
                                                     , pokemon=self.pokemons[self.player.rect.collidelist(self.pokemons)]))
            tp_list = list(self.objects['tp'].values())
            if self.player.feet.collidelist(tp_list) != -1:
                collided_house = tp_list[self.player.feet.collidelist(list(self.objects['tp'].values()))]
                pygame.event.post(pygame.event.Event(Event.TP, pos=(self.player.rect.x, self.player.rect.y),
                                                    house=list(self.objects['tp'].keys())[tp_list.index(collided_house)]))

        pygame.event.post(pygame.event.Event(Event.CUT_SCENE_START, cut_scene=self.tutorial))
        if True in pygame.key.get_pressed():
            pygame.event.post(pygame.event.Event(Event.KEY_PRESS, key=pygame.key.get_pressed()))

    def render(self):
        if Container.exists(Sprite.__name__):
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            for pokemon in self.pokemons:
                if pokemon not in self.player.inventory and pokemon not in self.group:
                    self.group.add(pokemon)
            if self.player.inventory_shown:
                self.player.show_inventory()
            else:
                self.player.inventory_menu.set_alpha(0)
        else:
            self.map_layer.center((71 * 16, 84 * 16))
            self.map_layer.draw(self.screen, self.screen.get_rect())
        self.quit_menu.render()

    def generate_pokemon(self):
        #pokemon_choice = random.randint(1, 153), random.randint(1, 153)
        for i in range(153):
            spawn_zone = random.choice(self.objects['spawn_pokemon'])
            spawn_coords = random.randint(spawn_zone.x, spawn_zone.x + spawn_zone.width) // 16, random.randint(spawn_zone.y,
                                                                                                         spawn_zone.y + spawn_zone.height) // 16
            pokemon = Container.get(LoaderInterface.__name__).load_from_index(Pokemon, i, x=spawn_coords[0], y=spawn_coords[1])
            if pokemon is not None:
                self.pokemons.append(pokemon)
        self.pokemons = random.sample(self.pokemons, 8)


