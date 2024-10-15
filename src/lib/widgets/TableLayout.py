import pygame.draw

from lib.widgets import Button
from lib.widgets.Widget import Widget


class TableLayout(Widget):
    def __init__(self, screen, x, y, width, height, **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)
        self.tables: dict = kwargs.get('tables')
        self.bg_color = '#6e4d4b'
        self.tables_buttons = [
            Button(screen, x + width / len(self.tables) * i, y, 0, 20, bg_color='#ff0000', color='#ffffff',
                   name=list(self.tables.keys())[i]) for i in range(len(self.tables.keys()))]
        self.background = self.tables[next(iter(self.tables))]
        for button in self.tables_buttons:
            button.set_action(self.table_change)
        self.rect = pygame.Rect(self.x, self.y + 20, self.width, self.height)

    def render(self):
        for button in self.tables_buttons:
            button.render()
        self.screen.blit(self.background, (self.x, self.y + 20), self.rect)
        self.background.update()

    def table_change(self, button):
        self.background = self.tables[button.name]

