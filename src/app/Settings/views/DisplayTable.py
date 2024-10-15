from abc import ABC

import pygame
from pygame import Surface

from lib.widgets import Button, Select


class DisplayTable(Surface, ABC):
    def __init__(self, x, y, size):
        super().__init__(size)
        self.view_resize_button = Button(self, 30 + x, 30 + y, 60, 20, name="Resize", fg_color=(255, 255, 255))
        self.save_button = Button(self, 30 + x, 70 + y, 120, 60, name="save")
        self.select = Select(self, 200 + x, 30 + y, 75, 30, name="Hello",
                             options=["1024x1080", '1920x1080', '960x640'])

    def update(self):
        self.fill(pygame.Color('#6e4d4b'))
        self.save_button.render()
        self.view_resize_button.render()
        self.select.render()
