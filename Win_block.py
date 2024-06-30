import pygame
class Win(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        win_image = pygame.image.load('sprites\\win_block.png').convert_alpha()
        self.image = win_image
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift