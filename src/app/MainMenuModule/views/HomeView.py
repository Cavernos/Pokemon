from abc import ABC
from pydoc import locate

from lib.views import View
from lib.widgets import Button


class HomeView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.buttons = []
        for objs in self.tmx_data.objectgroups:
            for obj in objs:
                if isinstance(locate(obj.type), Button.__class__):
                    self.buttons.append(Button(screen, obj.x, obj.y, obj.width, obj.height, obj.name))

    def update(self):
        self.group.draw(self.screen)
        for button in self.buttons:
            button.render()
