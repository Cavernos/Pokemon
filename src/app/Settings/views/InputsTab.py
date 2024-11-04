from abc import ABC

import pygame
from pygame import Surface

from lib.widgets import Button


class InputsTab(Surface, ABC):
    def __init__(self, x, y, size):
        super().__init__(size)
        self.view_resize_button = Button(self, 30 + x, 30 + y, 60, 20, name="Resize", fg_color=(255, 255, 255))
        self.save_button = Button(self, 30 + x, 70 + y, 120, 60, name="save")

    def update(self):
        self.fill(pygame.Color('#6e4d4b'))
        self.save_button.render()
        self.view_resize_button.render()
