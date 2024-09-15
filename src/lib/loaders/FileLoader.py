from pathlib import Path


class FileLoader:
    def __init__(self, definitions: list):
        self.definitions: list = definitions
        for definition in self.definitions:
            print(Path(definition).parent)

