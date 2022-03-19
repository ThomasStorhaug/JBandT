import pygame
from settings import *
from animation import Animate

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, groups, collision_sprites) -> None:
        super().__init__(groups)
        # display surface
        self.display_surface = pygame.display.get_surface()

        # sprite handling
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.image.get_rect()
        self.animation_controller = Animate(PlayerAnimationController)

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = 16
        self.collision_sprites = collision_sprites
        self.on_floor = False

        # player attributes
        self.sprite_type = 'player'
        self.health = 100
        self.health_bar = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE//4))
        self.health_rect = self.health_bar.get_rect()       
        self.health_rect.midbottom = (self.rect.centerx, self.rect.top - 128)
        self.hp_rect = self.health_bar.get_rect()
        self.hp_rect.topleft = self.health_rect.topleft

    def input(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[PL1_RIGHT]:
            self.direction.x = 1
        elif self.keys[PL1_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if self.keys[PL1_JUMP] and self.on_floor:
            self.direction.y = -self.jump_speed
        
        # For debugging healthbar:
        # if self.keys[pygame.K_RIGHT] and self.health < 100:
        #     self.health += 10
        # elif self.keys[pygame.K_LEFT] and self.health > 0:
        #     self.health -= 10

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0: # moving to the left
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0: # moving to the right
                    self.rect.right = sprite.rect.left
                    
    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0: # falling
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        if self.on_floor and self.direction.y != 0:
             self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def shoot_book(self):
        pass

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()

        # animation control

        self.animation_controller.set_state(self.direction, self.on_floor)
        self.animation_controller.update(self.image)


