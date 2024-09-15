from pathlib import Path


class Animal:
    def __init__(self, file):
        self.index = 0
        self.name = ""
        self.texture = Path()
        if self.__dict__.keys() == file.keys():
            for key, value in file.items():
                setattr(self, key, value)
        else:
            raise AttributeError(f"Could not load Pokemon: {file["name"] if "name" in file.keys() else ""}")