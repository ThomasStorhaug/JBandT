from concurrent.futures.process import _chain_from_iterable_of_lists
import pygame

from settings import CAMERA_BORDERS, HP_BG, HP_BORDER, HP_HP, TILE_SIZE, WIN_HEIGHT, WIN_WIDTH, WORLD_MAP
from player import Player
from tile import Tile
from debug import debug

class Level:
    def __init__(self) -> None:

        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.type = 'level'

        self.setup_level()

    def setup_level(self):
        for y_index, row in enumerate(WORLD_MAP):
            for x_index, tile in enumerate(row):
                x = x_index * TILE_SIZE
                y = y_index * TILE_SIZE
                if tile == 'X':
                    Tile((x, y), [self.visible_sprites, self.collision_sprites])
                if tile == 'P':
                    self.player = Player((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

    def run(self):
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

        # camera setup
        self.cam_left = CAMERA_BORDERS['left']
        self.cam_top = CAMERA_BORDERS['top']
        self.cam_width = self.display_surface.get_size()[0] - CAMERA_BORDERS['left'] - CAMERA_BORDERS['right']
        self.cam_height = self.display_surface.get_size()[1] - CAMERA_BORDERS['top'] - CAMERA_BORDERS['bottom']

        self.camera_rect = pygame.Rect(self.cam_left, self.cam_top, self.cam_width, self.cam_height)

    def custom_draw(self,player):
        # This camera setup will offset ALL SPRITES from their rect position -> Their rects position does not represent the sprites actual position
        # rather a reference point for the offset position.
        #
        # getting the camera position
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        # camera offset
        self.offset = pygame.math.Vector2(self.camera_rect.left - CAMERA_BORDERS['left'], self.camera_rect.top - CAMERA_BORDERS['top'])
        # This offset MUST be used when positioning and bliting ANY sprite on the canvas!

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset # When positioning anything on the screen this offset position is the reference.
            self.display_surface.blit(sprite.image, offset_pos)

            # draw healthbar:
            # Maybe use a separate sprite instance for healthbars.
            if sprite.sprite_type == 'player':
                #hp_offset_pos = (offset_pos[0], offset_pos[1] - 40)
                hp_width = round(sprite.health / 100 * 64)
                hp_rect = pygame.Rect(offset_pos[0], offset_pos[1] - 40, TILE_SIZE, TILE_SIZE//4)
                hphp_rect = pygame.Rect(offset_pos[0], offset_pos[1] - 40, hp_width, TILE_SIZE//4)
                pygame.draw.rect(self.display_surface, HP_BG, hp_rect, 0, 3)
                pygame.draw.rect(self.display_surface, HP_HP, hphp_rect, 0, 3)
                pygame.draw.rect(self.display_surface, HP_BORDER, hp_rect, 2, 3)

