from app.Sprite.actions import PlayerAction
from lib import Container
from lib.views import ViewHandler


class MapAction:
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        if hasattr(self.view_handler.get_view(), 'player'):
            self.player = self.view_handler.get_view().player
            PlayerAction()(self.player)




