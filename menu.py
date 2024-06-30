import pygame, sys, random
from zastar import zastavka1
from main import *
from help import myhelp
from pygame.color import THECOLORS
from pygame import font
pygame.init()
clock = pygame.time.Clock()
zastavka1(screen_w,screen_h,clock)
pygame.display.set_caption("Collector")
screen = pygame.display.set_mode([900, 800])
menu_image = pygame.image.load('menu1.png').convert()
play_image = pygame.image.load('play.png').convert()
help_image = pygame.image.load('help.png').convert()
exit_image = pygame.image.load('exit.png').convert()
obvodka = pygame.image.load('obvodka.png').convert_alpha()
play_rect = play_image.get_rect(topleft = (300,250))
help_rect = help_image.get_rect(topleft = (300,450))
exit_rect = exit_image.get_rect(topleft = (300,650))
running = True
while running:
    screen.blit(menu_image, (0, 0))
    screen.blit(play_image,(play_rect))
    screen.blit(help_image, (help_rect))
    screen.blit(exit_image, (exit_rect))
    (x, y) = pygame.mouse.get_pos()
    if exit_rect.collidepoint(x, y):
        screen.blit(obvodka,(exit_rect))
    if play_rect.collidepoint(x, y):
        screen.blit(obvodka,(play_rect))
    if help_rect.collidepoint(x, y):
        screen.blit(obvodka,(help_rect))
    print('x')

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(x,y):
                running = False

            if play_rect.collidepoint(x,y):
                game()
                print(2)
            if help_rect.collidepoint(x,y):
                myhelp()
                screen = pygame.display.set_mode([900, 800])
                print(3)
