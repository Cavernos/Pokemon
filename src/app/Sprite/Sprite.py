import os

from app.Sprite.actions import PlayerAction
from lib import Module


class Sprite(Module):

    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")
    def __init__(self):
        self.action = PlayerAction()