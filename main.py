import pygame, sys

from settings import *
from level import Level
from debug import debug
from menu import Menu

class Game:

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.clock = pygame.time.Clock()

        self.level = Menu(self)

    def run(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill(BG_COLOR)

            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()


"""
for frame_type in self.frames:
            for frame in range(1, self.frames[frame_type] + 1):
                self.states[frame_type].append(pygame.image.load('images/JB_' + frame_type + str(frame) + '.png').convert())
"""