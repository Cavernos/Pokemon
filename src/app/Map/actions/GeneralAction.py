from app.MainMenuModule.views import HomeView
from app.Map.views import MapView, HouseView
from app.Sprite import Sprite
from lib import Container


class GeneralAction:

    def on_key_press(self, event):
        if event.key in Container.get('inputs') and event.key not in Container.get('inputs')['player']:
            if hasattr(self, Container.get('inputs')[event.key]):
                getattr(self, Container.get('inputs')[event.key])(event.key)

    def return_to_main_menu(self, button):
        self.view_handler.set_view(HomeView)

    def escape_menu(self, button):
        if not self.escape_menu_shown:
            self.escape_menu_shown = True
            if Container.exists(Sprite.__name__):
                self.player.playable = False
            self.current_view.quit_menu.set_alpha(255)
            return
        else:
            self.escape_menu_shown = False
            if Container.exists(Sprite.__name__):
                self.player.playable = True
            self.current_view.quit_menu.set_alpha(0)
            return

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
