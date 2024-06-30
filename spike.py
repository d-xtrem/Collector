import pygame
class Spike(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        spike_image = pygame.image.load('sprites\\spike.png').convert_alpha()
        self.image = spike_image
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift