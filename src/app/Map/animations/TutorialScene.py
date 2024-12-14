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
        inputs_dict = Container.get('inputs')['player']
        self.dialogue = {}
        counter = 0
        already_played = False
        for key, value in inputs_dict.items():
            iteration = 2+3*counter
            if iteration == 14 and not already_played:
                self.dialogue[iteration-3] = self.dialogue[iteration-3] + f' and {pygame.key.name(key)} to {' '.join(value.split("_"))}'
                already_played = True
                counter -=1
            else:
                self.dialogue[iteration] = f'Press {pygame.key.name(key)} to {' '.join(value.split("_"))}'
            counter += 1
        self.dialogue[1] = "Hello and welcome in pokemon's world, in this tutorial, we will learn\nhow to play this game ?"
        self.dialogue[4] = "Ooh ! un pokemon abandonné, et si nous l'attrapions pour le sauver"
        self.dialogue[7] = "Parfait ! Maintenant, nous allons essayer de nous déplacer vers le bas"
        self.dialogue[10] = "Essayons de remonter en courant cette fois-ci"
        self.dialogue[13] = "Super ! Maintenant essayons de tourner à gauche"
        self.dialogue[16] = "Ce tutoriel est terminé ! Nous espérons qu'il vous a été utile"
        self.dialogue[17] = "Essayer donc maintenant de remplir votre inventaire de pokemons"
        self.text_counter = 0
        screen = pygame.display.get_surface()
        self.text_label = Label(screen, 0, 0, 0, 30, name='', color=(255,255, 255))
        self.menu = Menu(screen, 0, 0, screen.get_width(), self.text_label.height, self.text_label)
        self.running = True

    def update(self):
        self.player.playable = False
        space =  pygame.key.get_pressed()[pygame.K_SPACE]
        if hasattr(self, "start_pokemon"):
            self.start_pokemon.set_pos((79.5 * 16, 83.5 * 16))

        for i in range(16):
            if self.step%3 != 0:
                if int(self.text_counter) < len(self.dialogue[self.step]):
                    self.text_counter += 0.4
                else:
                    if space or self.step%3 == 2:
                        self.step += 1
                        self.text_counter = 0
                        break
            break
        if self.step == 0:
            if self.player.rect.y < 83.5*16:
                self.player.move_bottom(1)
                self.text_counter = 0
            else:
                self.step = 1
        if self.step == 3:
            if self.start_pokemon.rect.x - self.player.rect.x > 32:
                self.player.move_right(1)
                self.text_counter = 0
            else:
                self.step = 4
        if self.step == 6:
            if self.start_pokemon not in self.player.inventory or self.player.rect.x < 79.5*16:
                self.player.show_inventory()
                self.player.move_right(1)
            else:
                self.step = 7
        if self.step == 9:
            if self.player.rect.y < 91.5*16:
                self.player.move_bottom(1)
            else:
                self.step = 10
        if self.step == 12:
            if self.player.rect.y > 83.5*16:
                self.player.sprint(1)
                self.player.move_up(1)
            else:
                self.player.slow()
                self.step = 13
        if self.step == 15:
            if self.player.rect.x > 78*16:
                self.player.move_left(1)
            else:
                self.step = 16
        if self.step == 18:
            if self.start_pokemon in self.player.inventory or self.player.rect.y > 77*16:
                self.player.remove_from_inventory(self.start_pokemon)
                self.player.move_up(1)
            else:
                self.player.playable = True
                self.menu.set_alpha(0)
                self.running = False
        return self.running

    def render(self):
        if self.step % 3 != 0:
            self.text_label.set_name(self.dialogue[self.step][0:int(self.text_counter)])
            self.menu.set_height(self.menu.height * len(self.dialogue[self.step].splitlines()) +10)
        self.menu.render()


