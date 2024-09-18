import os.path
import sys
import tomllib
from pathlib import Path
from typing import Type

import pygame
import pygame.time
from pygame.event import Event

from app.module.views import HomeView
# from app.module.views import HomeView
from lib import Container, Module
from lib.events import EventListener
from lib.views import ViewHandler


class Window:
    def __init__(self):
        self.size: tuple = (960, 640)
        with open(os.path.join(Path(__file__).parent.parent.parent, "pyproject.toml"), "rb") as file:
            self.title: str = tomllib.load(file)['project']['name']
        self.running = False

    def run(self, event: Event):
        pygame.init()
        pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "img", "icon.png")))
        self.running = True
        view_handler = Container.get(ViewHandler.__name__)
        view_handler.set_view(HomeView)
        while self.running:
            view_handler.update()
            for e in pygame.event.get():
                EventListener.handle(e)

    @EventListener.add_event_listener(pygame.QUIT)
    def quit(self):
        pygame.quit()
        sys.exit(0)


class Game(Window):
    def __init__(self, definition):
        super().__init__()
        self.clock = pygame.time.Clock
        self.definition = definition
        self.modules = []

    def add_module(self, module: Type[Module]) -> object:
        self.modules.append(module)
        return self

    def run(self, event: Event):
        for module in self.modules:
            self.get_container().get(module.__name__)
        super().run(event)
        return self.handle(event)

    def get_container(self) -> Type[Container]:
        Container.add_definitions(self.definition)
        for module in self.modules:
            if module.definitions:
                Container.add_definitions(module.definitions)

        return Container

    def handle(self, event: Event):
        pass
