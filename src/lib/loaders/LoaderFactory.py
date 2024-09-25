import glob
import os

import app
from lib.loaders import FileLoader, DatabaseLoader, LoaderInterface


class LoaderFactory:
    def __call__(self) -> LoaderInterface:
        json_files = glob.glob(os.path.join(app.__path__[0], "**","*.json"))
        if not glob.glob(os.path.join(app.__path__[0], "**","*.json")):
            return DatabaseLoader()
        else:
            return FileLoader(json_files)
