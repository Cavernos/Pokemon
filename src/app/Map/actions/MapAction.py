import threading

import pygame.time

from app.Sprite.actions import PlayerAction
from lib import Container
from lib.views import ViewHandler


class MapAction:
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        if hasattr(self.view_handler.get_view(), 'player'):
            self.player = self.view_handler.get_view().player
            if Container.get('playable'):
                PlayerAction()(self.player)
            else:
                threading.Thread(daemon=True, target=self.cinematic).start()

    def cinematic(self):
        while self.player.rect.x <= 1328:
            self.player.move_right(1)
            pygame.time.wait(Container.get('clock').get_time())
        pygame.time.wait(Container.get('clock').get_time())
        while self.player.rect.y >= 200:
            pygame.time.wait(Container.get('clock').get_time())
            self.player.move_up(1)
