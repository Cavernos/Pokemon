import os
from pathlib import Path

from lib.Container import factory
from lib.events import EventListener
from lib.loaders import LoaderFactory, LoaderInterface
from lib.views import ViewHandler

config = {
    "version": "0.0.1",
    "SRC": os.path.join(Path(os.path.dirname(os.path.abspath(__file__))).parent, "src\\"),
    "APP": os.path.join(Path(os.path.dirname(os.path.abspath(__file__))).parent, "src", "app\\"),
    LoaderInterface.__name__: factory(LoaderFactory()),
    ViewHandler.__name__: ViewHandler(),
    EventListener.__name__: EventListener(),
    "views": {}
}



