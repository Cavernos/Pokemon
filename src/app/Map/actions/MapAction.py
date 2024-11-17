import pygame.time

from app.Battle import Battle
from app.Battle.views.BattleView import BattleView
from app.MainMenuModule.views import HomeView
from app.Sprite import Sprite
from app.Sprite.actions import PlayerAction, PokemonAction
from app.Sprite.entity import Player
from lib import Container
from lib.events import EventListener
from lib.views import ViewHandler


class MapAction:
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        self.current_view = self.view_handler.get_view()
        EventListener.add_event_listener(pygame.KEYDOWN, self.on_key_press)
        EventListener.add_event_listener(pygame.USEREVENT + 1, self.on_sprite_collide)
        self.current_view.accept_button.set_action(self.return_to_main_menu)
        self.current_view.discard_button.set_action(self.escape_menu)
        self.escape_press_counter = 0
        self.h_press_counter = 0
        if Container.exists(Sprite.__name__):
            self.player = self.current_view.player
            self.pokemon = self.current_view.pokemon
            PlayerAction()(self.player)
            PokemonAction()(self.pokemon)

    def on_key_press(self, event):
        if event.key in Container.get('inputs') and event.key not in Container.get('inputs')['player']:
            if hasattr(self, Container.get('inputs')[event.key]):
                getattr(self, Container.get('inputs')[event.key])(event.key)

    def return_to_main_menu(self, button):
        self.view_handler.set_view(HomeView)

    def escape_menu(self, button):
        self.escape_press_counter += 1
        if self.escape_press_counter > 1:
            self.escape_press_counter = 0
        if self.escape_press_counter == 1:
            if Container.exists(Sprite.__name__):
                self.player.playable = False
            self.current_view.quit_visible = True
        else:
            if Container.exists(Sprite.__name__):
                self.player.playable = True
            self.current_view.quit_visible = False

    def show_hitbox(self, event):
        for entity in self.current_view.entities:
            entity.show_hitbox()


    # def cinematic(self):
    #     while self.player.rect.x <= 1328:
    #         self.player.move_right(1)
    #         pygame.time.wait(Container.get('clock').get_time())
    #     pygame.time.wait(Container.get('clock').get_time())
    #     while self.player.rect.y >= 200:
    #         pygame.time.wait(Container.get('clock').get_time())
    #         self.player.move_up(1)
    def on_sprite_collide(self, event):
        if Container.exists(Battle.__name__):
            print('collide')
            #self.view_handler.set_view(BattleView)
