import json
import os.path

from app.module.actions.ModuleActions import ModuleActions
from app.module.entity import Animal
from lib import Module, Container
from lib.loaders import LoaderInterface, FileLoader


class ModuleClass(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        super().__init__()
        ModuleActions()
        loader: FileLoader = Container.get(LoaderInterface.__name__)
        with open(loader.json_file_path[os.path.dirname(os.path.abspath(__file__))], "r") as file:
            animal = Animal(json.loads(file.read()))
        print(animal.name)
