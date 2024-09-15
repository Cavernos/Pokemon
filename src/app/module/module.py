import os.path

from app.module.entity import Animal
from lib import Module


class ModuleClass(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        super().__init__()
        animal = Animal({})
