import os
from pathlib import Path


class FileLoader:
    json_file_path: dict = {}

    def __init__(self, definitions: list):
        self.definitions: list = definitions
        for definition in self.definitions:
            FileLoader.json_file_path[os.path.dirname(os.path.abspath(definition))] = os.path.join(Path(definition))
