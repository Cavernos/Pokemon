import os
from pathlib import Path

from lib.Container import factory
from lib.loaders import LoaderFactory, LoaderInterface

config = {
    "version": "0.0.1",
    "SRC": os.path.join(Path(os.path.dirname(os.path.abspath(__file__))).parent, "src\\"),
    LoaderInterface.__name__: factory(LoaderFactory())
}



