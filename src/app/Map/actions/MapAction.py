import pygame.time


from app.Map.actions.GeneralAction import GeneralAction
from app.Map.views import HouseView, MapView, PokemonStoreView
from app.Map.views.PokemonCenterView import PokemonCenterView
from app.Sprite import Sprite
from app.Sprite.actions import PlayerAction
from lib import Container
from lib.events import EventListener, Event
from lib.views import ViewHandler


class MapAction(GeneralAction):
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        self.current_view = self.view_handler.get_view()
        EventListener.add_event_listener(pygame.KEYDOWN, self.on_key_press)
        EventListener.add_event_listener(Event.COLLIDE, self.on_sprite_collide)
        EventListener.add_event_listener(Event.TP, self.on_house_door_collide)
        self.current_view.accept_button.set_action(self.return_to_main_menu)
        self.current_view.discard_button.set_action(self.escape_menu)
        self.escape_menu_shown = False
        self.h_press_counter = 0
        if Container.exists(Sprite.__name__):
            self.player = self.current_view.player
            self.pokemons = self.current_view.pokemons
            PlayerAction()(self.player)


    def on_sprite_collide(self, event):
        self.player.add_to_inventory(event.pokemon)
        if event.pokemon in self.player.inventory:
            self.current_view.group.remove(event.pokemon)
        # if Container.exists(Battle.__name__):
        #     print('collide')
        #     #self.view_handler.set_view(BattleView)

    def on_house_door_collide(self, event):
        if isinstance(self.current_view, MapView):
            Container.set('player', self.player)
            Container.set('pokemon', self.pokemons)
            if 'house' in event.house:
                self.view_handler.set_view(HouseView)
            elif 'pokemon_store' in event.house:
                self.view_handler.set_view(PokemonStoreView)
            else:
                self.view_handler.set_view(PokemonCenterView)


