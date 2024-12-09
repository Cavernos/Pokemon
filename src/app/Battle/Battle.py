import os

from app.Battle.actions import BattleAction
from lib import Module


class Battle(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        super().__init__()
        self.action = BattleAction()
