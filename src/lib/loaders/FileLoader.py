import json
import os
from pathlib import Path


class FileLoader:
    json_file_path: dict = {}

    def __init__(self, definitions: list):
        self.definitions: list = definitions
        for definition in self.definitions:
            FileLoader.json_file_path[os.path.dirname(os.path.abspath(definition))] = os.path.join(Path(definition))

    def load_from_json(self, classType, definition):
        with open(definition, 'rb') as file:
            return classType(json.loads(file.read()))
