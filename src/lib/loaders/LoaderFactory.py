import glob
import os

from lib.loaders import FileLoader, DatabaseLoader, LoaderInterface


class LoaderFactory:
    def __call__(self) -> LoaderInterface:
        json_files = glob.glob(os.path.join(os.getcwd(), "assets", "entities", "**", "*.json"))
        if not json_files:
            return DatabaseLoader()
        else:
            return FileLoader(json_files)
