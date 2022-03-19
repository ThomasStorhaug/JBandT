import pygame
from settings import *



class Button(pygame.sprite.Sprite):

    def __init__(self, pos:tuple, defaultimage:str, selectedimage:str, groups, func, **kwargs) -> None:
        super().__init__(groups)
        self.selected = False
        self.defaultimage = pygame.image.load(defaultimage)
        self.selectedimage = pygame.image.load(selectedimage)
        self.image = pygame.Surface((MENU_TILESIZE, MENU_TILESIZE), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = pos)
        self.func = func
        self.kwargs = kwargs

    def activate(self):
        if len(self.kwargs) > 0:
            self.func(self.kwargs['target'])
        else:
            self.func()
    
    def update(self, selected):

        if selected:
            self.selected = True
            self.image = self.selectedimage
        else:
            self.selected = False
            self.image = self.defaultimage

