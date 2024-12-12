import json
import os
from pathlib import Path


class FileLoader:
    json_file_path: dict = {}

    def __init__(self, definitions: list):
        self.definitions: list = definitions
        for definition in self.definitions:
            FileLoader.json_file_path[os.path.dirname(os.path.abspath(definition))] = os.path.join(Path(definition))

    def load_from_json(self, classType, definition, **kwargs):
        with open(definition, 'rb') as file:
            result = json.loads(file.read())
            result.update(kwargs)
            return classType(**result)

    def load_from_index(self, class_type, index, **kwargs):
        for key, value in FileLoader.json_file_path.items():
            if f"{index:03d}" in key:
                return self.load_from_json(class_type, value, **kwargs)
