from importlib.machinery import SourceFileLoader


class Container:
    config: dict = {}

    def __init__(self):
        self.config = Container.config

    @classmethod
    def get(cls, item: str) -> object | str:
        if item in cls.config.keys():
            return cls.config[item]
        return "Error"

    @classmethod
    def add_definitions(cls, definition):
        module_config = SourceFileLoader("config", definition).load_module().config
        cls.config.update(module_config)


def factory(factory: object) -> any:
    if callable(factory):
        return factory()
