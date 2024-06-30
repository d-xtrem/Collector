import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        door_image = pygame.image.load('sprites\\door.png').convert_alpha()
        self.image = door_image
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift