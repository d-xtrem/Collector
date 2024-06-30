import pygame
class Vrag(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        vrag_image = pygame.image.load('sprites\\vrag.png').convert_alpha()
        self.image = vrag_image
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5
    def update(self,x_shift):
        self.rect.x += x_shift
        self.rect.x += self.speed