import pygame
class Backgr(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        tile_image = pygame.image.load('tile.png').convert()
        self.image = tile_image
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift