import pygame

from app.Map.actions.GeneralAction import GeneralAction
from app.Map.views import MapView, HouseView
from app.Sprite import Sprite
from app.Sprite.actions import PlayerAction
from lib import Container
from lib.events import EventListener, Event
from lib.views import ViewHandler


class HouseAction(GeneralAction):
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        self.current_view = self.view_handler.get_view()
        EventListener.add_event_listener(pygame.KEYDOWN, self.on_key_press)
        EventListener.add_event_listener(Event.TP, self.on_house_door_collide)
        self.current_view.accept_button.set_action(self.return_to_main_menu)
        self.current_view.discard_button.set_action(self.escape_menu)
        self.escape_menu_shown = False
        self.h_press_counter = 0
        if Container.exists(Sprite.__name__):
            self.player = self.current_view.player
            PlayerAction()(self.player)

    def on_house_door_collide(self, event):
        if isinstance(self.current_view, HouseView):
            self.player.set_pos(event.pos)
            Container.set('player', self.player)
            self.view_handler.set_view(MapView)
