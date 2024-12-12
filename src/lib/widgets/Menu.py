import pygame.surface

from lib.widgets import Widget


class Menu(Widget):
    def __init__(self, screen, x, y, width, height, *widgets, **kwargs):
        super().__init__(screen, x, y, width, height, **kwargs)
        self.background = pygame.surface.Surface((width, height))
        self.widgets = []
        for widget in widgets:
            if isinstance(widget, Widget):
                widget.set_pos((widget.x + self.x,  widget.y + self.y))
            self.widgets.append(widget)


    def render(self):
        self.screen.blit(self.background, (self.x, self.y))
        for widget in self.widgets:
            if isinstance(widget, Widget):
                widget.render()

    def set_alpha(self, value):
        self.background.set_alpha(value)
        for widget in self.widgets:
            if isinstance(widget, Widget):
                widget.set_alpha(value)


    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def add_widget(self, widget):
        if isinstance(widget, Widget) and widget not in self.widgets:
            self.widgets.append(widget)
            widget.set_pos((widget.x + self.x, widget.y + self.y))
        else:
            del widget
    def remove_widget(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)

    def get_rect(self, **kwargs):
        self.background.get_rect(**kwargs)

