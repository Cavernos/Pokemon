import os

import pygame

from app.Sprite.entity import Entity
from lib import Container
from lib.widgets import Menu, Button
from lib.widgets.Label import Label


class Player(Entity):
    def __init__(self, x, y, width=100, height=128, *groups):
        # Constructeur Initialisation des différents paramètre de classe
        super().__init__(x, y, width, height, *groups)  # appel de la classe parente
        self.loaded_image = pygame.image.load(
            os.path.join(Container.get('ASSETS'), 'entities', 'player.png'))  # Chargement des données du joueur
        self.number_of_sprite = 4  # nombre d'image présente par ligne sur le joueur
        self.width = self.loaded_image.get_width() // 4  # longueur d'une seule image
        self.height = (self.loaded_image.get_height() // 4)  # largeur d'une seule image
        self.image = self.loaded_image.subsurface(
            (0, 0, self.width, self.height))  # Image qui apparait au lancement du jeu
        self.rect.size = self.width, self.height  # Boite de collision
        self.playable = True  # Jouable ou non jouable
        self.feet = pygame.Rect(self.x, self.y, self.width - 10, self.height * 0.5)  # Collision avec les pied du joueur
        # inventaire du joueur
        self.inventory = []
        self.inventory_menu = Menu(pygame.display.get_surface(), 0, 0, 192, 62)
        self.inventory_menu.y = pygame.display.get_surface().get_height() - self.inventory_menu.height
        self.inventory_shown = False

    # Update actualise les mouvements du joueur
    def update(self, *args, **kwargs):
        func_name = args[0]
        old_position = [self.rect.x, self.rect.y].copy()
        if hasattr(self, func_name):
            getattr(self, func_name)(1)
        self.position = [self.rect.x, self.rect.y].copy()
        self.feet.midbottom = self.rect.midbottom
        if self.feet.collidelist(self.obstacles) != -1:
            self.position = old_position
            self.rect.topleft = old_position
            self.feet.midbottom = self.rect.midbottom

    def add_to_inventory(self, item):
        """Ajout d'un pokemon dans l'inventaire"""
        if item not in self.inventory and len(self.inventory) < 6:
            self.inventory.append(item)

    def remove_from_inventory(self, item):
        for pokemon in self.inventory:
            if pokemon.index == item.index:
                self.inventory.remove(pokemon)
                pokemon.set_pos(
                    (self.rect.x + self.direction[0] * self.width, self.rect.y + self.direction[1] * self.height))
        self.inventory_menu.remove_widget(item)
        del item

    def show_inventory(self):
        screen = pygame.display.get_surface()
        self.inventory_menu.set_alpha(255)
        if len(self.inventory_menu.widgets) != len(self.inventory):
            self.inventory_menu.widgets.clear()
            for i in range(len(self.inventory)):
                    pokemon = self.inventory[i]
                    button = Button(screen, pokemon.width * i, 0, pokemon.width, pokemon.height,
                                    image=pokemon.back_image, index=pokemon.index)
                    button.set_action(self.remove_from_inventory)
                    self.inventory_menu.add_widget(button)
            if len(self.inventory) == 6:
                self.inventory_menu.add_widget(
                    Label(pygame.display.get_surface(), 0, 32, 0, 25, name="Inventaire plein", color="#ffffff"))
        self.inventory_menu.render()
