import threading

import pygame

from lib import Container


class PokemonAction:
    def __call__(self, *args, **kwargs):
        self.pokemon = args[0]
        threading.Thread(daemon=True, target=self.move).start()

    def move(self):
        while True:
            x_coord, y_coord = self.pokemon.x, self.pokemon.y
            while self.pokemon.rect.x <= x_coord + 10:
                self.pokemon.move_right(1)
                pygame.time.wait(Container.get('clock').get_time())
            while self.pokemon.rect.y >= y_coord - 10:
                self.pokemon.move_up(1)
                pygame.time.wait(Container.get('clock').get_time())
            while self.pokemon.rect.x >= x_coord - 10:
                self.pokemon.move_left(1)
                pygame.time.wait(Container.get('clock').get_time())
            while self.pokemon.rect.y <= y_coord + 5:
                self.pokemon.move_bottom(1)
                pygame.time.wait(Container.get('clock').get_time())

            pygame.time.wait(Container.get('clock').get_time())
