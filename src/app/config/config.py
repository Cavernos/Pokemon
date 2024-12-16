import os
from pathlib import Path

from app.MainMenuModule.views import HomeView
from lib.Container import factory
from lib.animations import CutSceneManager
from lib.events import EventListener
from lib.loaders import LoaderFactory, LoaderInterface
from lib.views import ViewHandler
config = {
    "VERSION": "0.0.1",
    "FPS": 60,
    "SIZE": (960, 640),
    "APP": Path(os.path.dirname(__file__)).parent,
    "ASSETS": os.path.join(Path(os.path.dirname(__file__)).parent, "assets\\"),
    LoaderInterface.__name__: factory(LoaderFactory()),
    ViewHandler.__name__: ViewHandler(),
    EventListener.__name__: EventListener(),
    CutSceneManager.__name__: CutSceneManager(),
    "views": {},
    "FIRST_VIEW": HomeView
}



