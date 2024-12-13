import pygame.display

from lib import Container
from lib.widgets import Menu
from lib.widgets.Label import Label


class TutorialScene:
    def __init__(self, player, start_pokemon):
        self.player = player
        self.name = 'tutorial'
        self.step = 0
        inputs_dict = Container.get('inputs')['player']
        self.dialogue = {}
        iteration = 0
        for key, value in inputs_dict.items():
            iteration += 1
            self.dialogue[iteration] = f'Press {pygame.key.name(key)} to {' '.join(value.split("_"))}'
        self.text_counter = 0
        screen = pygame.display.get_surface()
        self.text_label = Label(screen, 0, 20, 0, 30, name='', color=(255,255, 255))
        self.menu = Menu(screen, 0, 0, screen.get_width(), self.text_label.height*2, self.text_label)
        self.running = True

    def update(self):
        self.player.playable = False
        if self.step == 0:
            if int(self.text_counter) < len(self.dialogue[2]):
                self.text_counter += 0.4
            else:
                self.step = 1
        if self.step == 1:
            if self.player.rect.x < self.player.x + 96:
                self.player.move_right(1)
                self.text_counter = 0
            else:
                self.step = 2
        if self.step == 2:
            if int(self.text_counter) < len(self.dialogue[3]):
                self.text_counter += 0.4
            else:
                self.step = 3
        if self.step == 3:
            if self.player.rect.y > self.player.y - 32:
                self.player.move_up(1)
                self.text_counter = 0
            else:
                #self.step = 4
                self.player.playable = True
                self.menu.set_alpha(0)
                self.running = False
        return self.running

    def render(self):
        if self.step == 0:
            self.text_label.set_name(self.dialogue[2][0:int(self.text_counter)])
        if self.step == 2:
            self.text_label.set_name(self.dialogue[3][0:int(self.text_counter)])
        self.menu.render()


