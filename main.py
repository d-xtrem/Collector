import sys

from level1 import *
from levelpy import *
def game():

    pygame.init()
    screen = pygame.display.set_mode((screen_w,screen_h))
    pygame.display.set_caption('Collector')
    clock = pygame.time.Clock()
    level = Level(level_map,screen)
    level2 = Level(level_map2,screen)
    level3 = Level(level_map3,screen)
    level4 = Level(level_map4,screen)
    level5 = Level(level_map5, screen)
    level.level = True


    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if level.level == True:
            if level.hero:
                level.run()
        #следующий
            if level.player.sprite.rect.centery > screen_h or keys[pygame.K_t] == True:
                level.level = False
                level2.level = True
                level2.player.sprite.coinwallet = level.player.sprite.coinwallet
        #рестарт уровня
            if level.player.sprite.rect.centery < 0 or keys[pygame.K_o] == True:
                del level
                level = Level(level_map, screen)
                level.level = True


        if level2.level == True:
            if level2.hero:
                level2.run()
            else:
                del level2
                level2 = Level(level_map2, screen)
                level2.level = True

        #следующий
            if level2.player.sprite.rect.centery > screen_h or keys[pygame.K_y] == True:
                level3.level = True
                level2.level = False
                level3.player.sprite.coinwallet = level2.player.sprite.coinwallet
        #рестарт уровня
            if keys[pygame.K_o] == True or level2.player.sprite.rect.centery < 0:
                del level2
                level2 = Level(level_map2, screen)
                level2.level = True
        if level3.level == True:
            if level3.hero:
                level3.run()
            else:
                del level3
                level3 = Level(level_map3, screen)
                level3.level = True
                level3.player.sprite.coinwallet = level2.player.sprite.coinwallet

            if level3.player.sprite.rect.centery > screen_h or keys[pygame.K_u] == True:
                level4.level = True
                level3.level = False
                level4.player.sprite.coinwallet = level3.player.sprite.coinwallet

        if keys[pygame.K_p] == True or level3.player.sprite.rect.centery < 0:
            del level3
            level3 = Level(level_map3, screen)
            level3.level = True
            level3.player.sprite.coinwallet = level2.player.sprite.coinwallet

        if level4.level == True:
            if level4.hero:
                level4.run()
            else:
                del level4
                level4 = Level(level_map4, screen)
                level4.level = True
                level4.player.sprite.coinwallet = level3.player.sprite.coinwallet
        if level4.player.sprite.rect.centery > screen_h or keys[pygame.K_i] == True:
            level5.level = True
            level4.level = False
            level3.level = False
            level2.level = False
            level.level = False
            level5.player.sprite.coinwallet = level4.player.sprite.coinwallet


        if level5.level:
            level5.run()
        if level5.player.sprite.rect.centery < 0:
            del level5
            level5 = Level(level_map5, screen)
            level5.level = True
            level5.player.sprite.coinwallet = level4.player.sprite.coinwallet






        pygame.display.update()
        clock.tick(60)
        if keys[pygame.K_ESCAPE]:
            return
