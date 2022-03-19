from typing import Collection
import pygame
from utilities import *

WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = (1280, 720)
FPS = 60

WORLD_MAP = [
    '                                                  ',
    '             XXXXX    XXXXX                       ',
    '                                                  ',
    '                     XXXXX                        ',
    '                                                  ',
    '                           XXXXX                  ',
    '                                                  ',
    '                                 XXXXX            ',
    '                                                  ',
    '             XXXXX                     XXXXX      ',
    '       P                                          ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]

TILE_SIZE = 32
PLAYER_SIZE = 38
COLORS = [
    '0d2b45', # 0
    '203c56', # 1
    '544e68', # 2
    '8d697a', # 3
    'd08159', # 4
    'ffaa5e', # 5
    'ffd4a3', # 6
    'ffecd6', # 7
]

BG_COLOR = convertToRGB(COLORS[0])
PLAYER_COLOR = convertToRGB(COLORS[6])
TILE_COLOR = convertToRGB(COLORS[3])

HP_BG = convertToRGB(COLORS[1])
HP_HP = convertToRGB(COLORS[6])
HP_BORDER = convertToRGB(COLORS[2])

CAMERA_BORDERS = {
    'left': 100,
    'right': 200,
    'top': 100,
    'bottom': 150
}

# Input controls
# Player 1:

PL1_RIGHT = pygame.K_RIGHT
PL1_LEFT = pygame.K_LEFT
PL1_JUMP = pygame.K_SPACE
PL1_ABI1 = pygame.K_1
PL1_ABI2 = pygame.K_2


class PlayerAnimationController:
    def __init__(self) -> None:
        # animation attributes
        self.states = {
            'idle': [],
            'run': [],
        }

        self.frames = {
            'idle': 4,
            'run': 6
        }
        self.transitions = {}
        self.random_states = False
        self.blit = (- 80, -48)

        for frame_type in self.frames:
            for frame in range(1, self.frames[frame_type] + 1):
                self.states[frame_type].append(pygame.image.load('images/JB_' + frame_type + str(frame) + '.png').convert_alpha())

        
MENU_TILESIZE = 16
        
MENU_LAYOUT = [
    '                                                                                ',
    '                                                                              X ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                    L                                           ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
    '                                                                                ',
]