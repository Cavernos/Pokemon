from importlib.machinery import SourceFileLoader


class Container:
    def __init__(self):
        self.config: dict = {}

    def get(self, item: str) -> object | str:
        if item in self.config.keys():
            return self.config[item]
        return "Error"

    def add_definitions(self, definition):
        module = SourceFileLoader("config", definition).load_module().config
        self.config.update(module)
