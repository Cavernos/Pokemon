import pygame

from app.Map import Map
from app.Map.actions import MapAction
from app.Map.views import MapView

config = {
    Map.__name__: Map(),
    "views": {
        MapView.__name__: MapView

    },
    "inputs": {
        pygame.K_ESCAPE: MapAction.escape_menu.__name__
    }

}
