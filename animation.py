import pygame, sys
from settings import *
from debug import debug

class Animate:
    def __init__(self, animation_controller) -> None:
        # Initiate the object that will be animated
        self.animation_controller = animation_controller()

        self.states = self.animation_controller.states # dict -> {idle, run, randomstates}

        self.animation_speed = 3 # This is the number of frames between each animated frame
        self.frame_counter = 0 # This counts frames, up to animation_speed
        self.animation_frame = 0 # this controls which frame is being blitted to the surface
        self.state = 'idle'
        self.facing_left = False # If the sprites are only alligned to the right, will be used to flip the sprite, probably not optimal
        self.last_state = 'idle'

    def update(self, surface:pygame.Surface):
        if self.frame_counter < self.animation_speed:
            self.frame_counter += 1
        else:
            self.frame_counter = 0
            if self.animation_frame < self.animation_controller.frames[self.state] - 1:
                self.animation_frame += 1
            else:
                self.animation_frame = 0
        if self.animation_frame > len(self.states[self.state]) - 1:
            self.animation_frame = 0
        self.frame = self.states[self.state][self.animation_frame]
        self.frame_rect = self.frame.get_rect()

        debug(('Frame dict: ', len(self.animation_controller.states['run'])), pygame.display.get_surface())
        #print(self.frame_count)
        if self.facing_left:
            self.frame = pygame.transform.flip(self.frame, True, False)
        
        surface.fill((0, 0, 0, 0))
        surface.blit(self.frame, (0,0))

    def set_state(self, dir_vector:pygame.math.Vector2, on_floor:bool):
        self.last_state = self.state
        
        # determine state
        if on_floor:
            if 'run' in self.states:
                if dir_vector.x > 0:
                    self.state = 'run' # assuming the sprites only have a right allignment
                    self.facing_left = False
                elif dir_vector.x < 0:
                    self.state = 'run'
                    self.facing_left = True
                else:
                    self.state = 'idle'
                

"""
pygame.init()

scr = pygame.display.set_mode((500, 500))

vec = pygame.math.Vector2(1, 0)
animate = Animate(PlayerAnimationController)
animate.set_state(vec, True)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    scr.fill('white')
    animate.update(scr)
    pygame.display.update()
    clock.tick(60)
"""