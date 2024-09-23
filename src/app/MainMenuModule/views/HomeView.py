from abc import ABC

from lib.views import View
from lib.widgets import Button


class HomeView(View, ABC):
    def __init__(self, screen):
        super().__init__(screen)
        self.button = [Button(self.screen, 120, 60, 200, 200, "hello"), Button(self.screen, 400, 400, 200, 200, "hello2")]

    def update(self):
        self.group.draw(self.screen)
        for button in self.button:
            button.render()
