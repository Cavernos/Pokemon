import random

import pygame

from lib.widgets import Menu
from lib.widgets.Label import Label


class HouseScene:
    def __init__(self):

        self.name = 'Hous_scen'
        self.step = 0
        self.dialogue = {
            0: "Go outside !!!",
            1: "Good Luck in your game",
            2: "I want to help you but I don't know how",
            3: "Your are the best in this game",
            4: "Don't forget to go in the pokemon center for more information"
        }
        self.dialogue_choice = random.randint(0, len(list(self.dialogue.keys()))-1)
        self.text_counter = 0
        screen = pygame.display.get_surface()
        self.text_label = Label(screen, 10, 0, 0, 30, name='', color=(255, 255, 255))
        self.menu = Menu(screen, 0, 0, screen.get_width(), self.text_label.height, self.text_label)
        self.running = True

    def update(self):
        if self.step == 0:
            if int(self.text_counter) < len(self.dialogue[self.dialogue_choice])+10:
                self.text_counter += 0.4
            else:
                self.menu.set_alpha(0)
                self.running = False
        return self.running

    def render(self):
        self.text_label.set_name(self.dialogue[self.dialogue_choice][0:int(self.text_counter)])
        self.menu.set_height(self.menu.height * len(self.dialogue[self.step].splitlines()) + 10)
        self.menu.render()


