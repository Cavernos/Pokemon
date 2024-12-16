import pygame

from app.Sprite import Sprite, entity

config = {
    Sprite.__name__: Sprite(),
    "inputs": {
        "player": {
            pygame.K_d: entity.Player.move_right.__name__,
            pygame.K_e: entity.Player.show_inventory.__name__,
            pygame.K_s: entity.Player.move_bottom.__name__,
            pygame.K_z: entity.Player.move_up.__name__,
            pygame.K_LSHIFT: entity.Player.sprint.__name__,
            pygame.K_q: entity.Player.move_left.__name__,
        }
    }

}
