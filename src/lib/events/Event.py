import pygame.constants


class Event:
    KEY_PRESS = pygame.constants.USEREVENT
    COLLIDE = pygame.constants.USEREVENT + 1
    TP = pygame.constants.USEREVENT + 2
    CUT_SCENE_START = pygame.constants.USEREVENT + 3
    CUT_SCENE_STOP = pygame.constants.USEREVENT + 4