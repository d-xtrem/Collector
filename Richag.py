import pygame
bottom_image = pygame.image.load('sprites\\bottom.png')
class Richag(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = bottom_image
        self.rect = self.image.get_rect(topleft = pos)
        self.active = False
    def update(self,x_shift):
        self.rect.x += x_shift