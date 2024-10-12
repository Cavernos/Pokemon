from abc import ABC
from pydoc import locate

from lib.views import TiledView
from lib.widgets import Button


class HomeView(TiledView, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        for objs in self.tmx_data.objectgroups:
            for obj in objs:
                if isinstance(locate(obj.type), Button.__class__):
                    self.buttons.append(locate(obj.type)(screen, obj.x, obj.y, obj.width, obj.height, transparent=True))
        print(self.buttons)
        #if Container.exists(SettingsView.__name__):
            # self.buttons.append(Button(screen, 260, 52, 44, 44, "Settings"))

    def update(self):
        super().update()
        for button in self.buttons:
            button.render()
