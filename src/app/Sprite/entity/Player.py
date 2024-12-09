import os

import pygame

from app.Sprite.entity import Entity
from lib import Container


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
