import pygame

from app.MainMenuModule.views import HomeView
from lib import Container
from lib.events import Event, EventListener
from lib.views import ViewHandler


class SettingsActions:
    def __call__(self, *args, **kwargs):
        self.view_handler = Container.get(ViewHandler.__name__)
        #self.view_handler.get_view().view_resize_button.set_action(self.resize)
        self.view_handler.get_view().display_table.background.save_button.set_action(self.save)
        self.view_handler.get_view().display_table.background.select.on_action(self.resize)
        EventListener.add_event_listener(pygame.KEYDOWN, self.return_to_main)

    def resize(self, option):
        self.view_handler.get_view().display_table.background.select.on_click(option)
        self.view_handler.get_view().display_table.background.select.selected_button.set_name(option.name)
        if Container.exists("SIZE"):
            Container.set("SIZE", tuple(int(i) for i in option.name.split('x')))
            print(Container.get('SIZE'))

    def save(self, button):
        pygame.display.set_mode(Container.get('SIZE'), flags=pygame.RESIZABLE)

    def return_to_main(self, event):
        self.view_handler.set_view(HomeView)