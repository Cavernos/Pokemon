from typing import Type

import pygame.time
from pygame.event import Event

from lib import Container, Module


class Game:
    def __init__(self, definition):
        self.clock = pygame.time.Clock
        self.definition = definition
        self.modules = []

    def add_module(self, module: Type[Module]) -> object:
        self.modules.append(module)
        return self

    def run(self, event: Event):
        for module in self.modules:
            self.get_container().get(module.__name__)
        return self.handle(event)

    def get_container(self) -> Type[Container]:
        Container.add_definitions(self.definition)
        for module in self.modules:
            if module.definitions:
                Container.add_definitions(module.definitions)

        return Container

    def handle(self, event: Event):
        pass
