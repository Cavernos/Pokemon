from app.Map import Map
from app.Map.views import MapView

config = {
    Map.__name__: Map(),
    "views": {
        MapView.__name__: MapView

    }

}
