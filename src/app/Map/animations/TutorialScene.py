import pygame.display

from lib import Container
from lib.widgets import Menu
from lib.widgets.Label import Label


class TutorialScene:
    def __init__(self, player, start_pokemon):
        self.player = player
        self.start_pokemon = start_pokemon
        self.name = 'tutorial'
        self.step = 0
        self.step_max = 7
        inputs_dict = Container.get('inputs')['player']
        self.dialogue = {}
        iteration = 0
        for key, value in inputs_dict.items():
            self.dialogue[iteration] = f'Press {pygame.key.name(key)} to {' '.join(value.split("_"))}'
            iteration += 1
        self.text_counter = 0
        screen = pygame.display.get_surface()
        self.text_label = Label(screen, 0, 20, 0, 30, name='', color=(255,255, 255))
        self.menu = Menu(screen, 0, 0, screen.get_width(), self.text_label.height*2, self.text_label)
        self.running = True

    def update(self):
        self.player.playable = False
        for i in range(self.step_max):
            if self.step == i:
                if int(self.text_counter) < len(self.dialogue[i//2]):
                    self.text_counter += 0.4
                else:
                    self.step = i+1
                    break
        if self.step == 1:
            if self.player.rect.x < self.player.x + 96:
                self.player.move_right(1)
                self.text_counter = 0
            else:
                self.step = 2
        if self.step == 3:
            if self.player.rect.y > self.player.y - 32:
                self.player.move_up(1)
                self.text_counter = 0
            else:
                self.step = 4
        if self.step == 5:
            if self.player.rect.x > self.player.x:
                self.player.move_left(1)
                self.text_counter = 0
            else:
                self.step = 6
        if self.step == 7:
            if self.player.rect.y < self.player.y:
                self.player.move_bottom(1)
                self.text_counter = 0
            else:
                self.step = 8

        if self.step == 8:
            self.start_pokemon.set_pos((self.player.x + self.player.width+10, self.player.y))
            if not self.player.rect.collidepoint(self.start_pokemon.rect.topleft):
                self.player.move_right(1)
            else:
                self.step = 9
                self.player.playable = True
                self.menu.set_alpha(0)
                self.running = False
        return self.running

    def render(self):
        if self.step % 2 == 0:
            self.text_label.set_name(self.dialogue[self.step//2][0:int(self.text_counter)])
        self.menu.render()


