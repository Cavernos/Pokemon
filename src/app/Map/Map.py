import os

from app.Map.actions import MapAction
from lib import Module
from Player import Player

class Map(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")
    
    def __init__(self):
        self.action = MapAction()
    def add_player(self, player) :
            self.group.add(player)
            self.player = player
            self.Player = None
    def update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())
        self.Player.align_hitbox()
