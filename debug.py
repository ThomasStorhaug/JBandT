from typing import Iterable
import pygame
pygame.init()
font = pygame.font.Font(None, 30)


def debug(info:Iterable, surface:pygame.Surface, y = 10, x = 10):
    # info is the parameter that will be displayed on screen, can be an iterable
    display_surface = surface
    text_list = []
    if type(info) != str:
        for item in info:
            text_list.append(str(item))
    text = ' '.join(text_list)
    debug_surf = font.render(text, True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)