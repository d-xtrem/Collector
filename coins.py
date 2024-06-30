import pygame
class Coin(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        coin_image = pygame.image.load('sprites\\coin.png').convert_alpha()
        self.image = coin_image
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift