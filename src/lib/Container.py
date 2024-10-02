import logging
from importlib.machinery import SourceFileLoader
from typing import Any


class Container:
    config: dict = {}

    def __init__(self):
        self.config = Container.config

    @classmethod
    def get(cls, item: str) -> Any:
        if item in cls.config.keys():
            return cls.config[item]
        for value in cls.config.values():
            if isinstance(value, dict):
                if item in value:
                    return value[item]
        logging.getLogger(__name__).warning(f"Could not load {item}")
        return None

    @classmethod
    def add_definitions(cls, definition: str | dict):
        if isinstance(definition, str):
            module_config = SourceFileLoader("config", definition).load_module().config
        else:
            module_config = definition
        for key, value in module_config.items():
            if isinstance(value, dict):
                if key in cls.config.keys():
                    module_config[key] = {**module_config[key], **cls.config[key]}
        cls.config = cls.config | module_config

    @classmethod
    def set(cls, key, value):
        cls.config[key] = value

    @classmethod
    def exists(cls, key):
        if key in cls.config.keys():
            return True
        for value in cls.config.values():
            if isinstance(value, dict):
                if key in value:
                    return True
        return False


def factory(factory: object) -> any:
    if callable(factory):
        return factory()
