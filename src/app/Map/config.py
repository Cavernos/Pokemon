import pygame

from app.Map import Map
from app.Map.actions import GeneralAction
from app.Map.views import MapView, HouseView

config = {
    Map.__name__: Map(),
    "views": {
        MapView.__name__: MapView,
        HouseView.__name__: HouseView
    },
    "inputs": {
        pygame.K_ESCAPE: GeneralAction.escape_menu.__name__,
        pygame.K_h: GeneralAction.show_hitbox.__name__
    }

}
