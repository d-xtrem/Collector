import pygame
from levelpy import *


class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        player_image = pygame.image.load('sprites\\player.png').convert()
        self.image = player_image
        self.rect = self.image.get_rect(topleft = pos)


        #Движение
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.95
        self.jump_speed = -18
        self.ground = False
        self.coinwallet = 0

        self.press_e = False

    def get_input(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            self.direction.x = 0
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            if self.ground:
                self.jump()



    def apply_gravity(self):

        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        if self.direction.y == 0 :
            self.ground = True
        else:
            self.ground = False

