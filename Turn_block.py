import pygame
class Turn_block(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        super().__init__()
        #изменил
        self.rect = pygame.Rect((x,y,size,size))
    def update(self,x_shift):
        self.rect.x += x_shift