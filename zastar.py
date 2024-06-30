import pygame, sys
from pygame.color import THECOLORS
from pygame import font
pygame.init()
pygame.display.set_caption("Collector")
def zastavka1(screen_w,screen_h,clock):
    screen = pygame.display.set_mode([screen_w, screen_h])
    zastav = pygame.image.load('zastavochka.png').convert()
    font = pygame.font.Font(None, 40)
    text = pygame.image.load('pressanykey.png')
    pygame.display.flip()
    running = True
    while running:
        screen.blit(zastav, [0, 0])

        screen.blit(text, [350, 560])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        pygame.display.update()
        clock.tick(60)








