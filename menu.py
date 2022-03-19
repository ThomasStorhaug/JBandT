import pygame, sys

from settings import *
from button import Button
from level import Level
from debug import debug

def exit_game():
    pygame.quit()
    sys.exit()

def select_level(obj):
    obj.level = Level()

class Menu:

    def __init__(self, main_obj) -> None:
        self.buttons = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()
        self.type = 'menu'
        self.select_level = 'menu'
        self.main_obj = main_obj
        self.setup_menu()
        
    def setup_menu(self):
        for y_index, row in enumerate(MENU_LAYOUT):
            for x_index, tile in enumerate(row):
                x = x_index * MENU_TILESIZE
                y = y_index * MENU_TILESIZE
                if tile == 'X':
                    Button((x, y), 'images/button_exit1.png', 'images/button_exit2.png', self.buttons, exit_game)
                if tile == 'L':
                    Button((x, y), 'images/button_level1.png', 'images/button_level2.png', self.buttons, select_level, target=self.main_obj)

    def input(self):
        self.pressed = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons.sprites():
            if button.rect.collidepoint(self.mouse_pos):
                if self.pressed[0]:
                    button.update(True)
                    button.activate()
            else:
                self.buttons.update(False)

    def run(self):
        self.input()
        self.buttons.draw(self.display_surface)
        debug(('select_level: ', self.select_level), self.display_surface)
        