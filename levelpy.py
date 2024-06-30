import pygame,sys
from tiles import Tile
from spike import Spike
from level1 import tile_size, screen_w, screen_h
from player import Player
from coins import  Coin
from Richag import Richag
from door import Door
from Vrag import Vrag
from Win_block import Win
from Turn_block import Turn_block


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.step = 0
        self.hero = True
        self.level = False
        background = pygame.image.load('sprites\\background1.png').convert()
        self.background = background
        self.x = 0
        self.richage = False
        self.wine = False
        self.win_act = False



    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.richag = pygame.sprite.GroupSingle()
        self.doors = pygame.sprite.Group()
        self.vrags = pygame.sprite.Group()
        self.turn_blocks = pygame.sprite.Group()
        self.win_block = pygame.sprite.GroupSingle()
        #индекс ряда в дата левеле
        for row_index, row in enumerate(layout):
            #позиция в ряде и проверка строки
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'D':
                    door = Door((x,y),tile_size)
                    self.doors.add(door)
                if cell == 'T':
                    spike = Spike((x,y),tile_size)
                    self.spikes.add(spike)
                if cell == 'O':
                    coin = Coin((x,y),tile_size)
                    self.coins.add(coin)
                if cell == 'V':
                    vrag = Vrag((x,y),tile_size)
                    self.vrags.add(vrag)
                if cell == 'R':
                    richag_sprite = Richag((x,y), tile_size)
                    self.richag.add(richag_sprite)
                if cell == 'P':
                    player_sprite = Player((x, y - tile_size))
                    self.player.add(player_sprite)
                if cell == 'B':
                    turn_block = Turn_block(x,y,tile_size)
                    self.turn_blocks.add(turn_block)
                if cell == 'W':
                    win_sprite = Win((x,y),tile_size)
                    self.win_block.add(win_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_w//2 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_w - screen_w//2 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        richag = self.richag.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        for sprite in self.doors.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        if len(self.richag) == 1:
            if richag.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = richag.rect.right
                elif player.direction.x > 0:
                    player.rect.right = richag.rect.left


    def vertical_movement_collision(self):
        player = self.player.sprite
        richag = self.richag.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom

                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

        if len(self.doors) > 0:
            for sprite in self.doors.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom

                    elif player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0


        if len(self.richag) == 1:
            if richag.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = richag.rect.bottom

                elif player.direction.y > 0:
                    player.rect.bottom = richag.rect.top
                    player.direction.y = 0
    def spike_collision(self):
        player = self.player.sprite
        for sprite in self.spikes.sprites():
            if sprite.rect.colliderect(player.rect):
                self.hero = False


    def coin_collision(self):
        # global coinwallet
        player = self.player.sprite
        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect):
                player.coinwallet += 1
                sprite.kill()
                print(player.coinwallet)

    def richag_activated(self):
        player = self.player.sprite
        richag = self.richag.sprite
        print(player.coinwallet)
        if (richag.rect.left == player.rect.right and richag.rect.top >= player.rect.bottom and richag.rect.bottom >= richag.rect.top ) or (richag.rect.right == player.rect.left and richag.rect.top <= player.rect.bottom and richag.rect.bottom >= richag.rect.top ) or (richag.rect.top == player.rect.bottom and richag.rect.left <= player.rect.right and richag.rect.right >= player.rect.left) or ((richag.rect.bottom == player.rect.top and richag.rect.left <= player.rect.right and richag.rect.right >= player.rect.left)):
            player.press_e = True
            self.richage = True
            print('касаемся')
        else:
            player.press_e = False
            self.richage = False
    def richag_input(self):
        keys = pygame.key.get_pressed()
        player = self.player.sprite
        richag = self.richag.sprite
        if keys[pygame.K_e]:
            if player.press_e and player.coinwallet >= 5 and self.richage == True:
                richag.active = True
                player.coinwallet -= 5

    def doors_open(self):
        richag = self.richag.sprite
        if richag.active:
            for sprite in self.doors.sprites():
                sprite.kill()

    def vrag_turn(self):
        for vrag in self.vrags.sprites():
            for sprite in self.turn_blocks.sprites():
                if vrag.rect.center == sprite.rect.center:
                    vrag.speed = -vrag.speed

    def vrag_collision(self):
        player = self.player.sprite
        for sprite in self.vrags.sprites():
            if sprite.rect.colliderect(player.rect):
                self.hero = False

    def background_scroll(self):
        self.x += self.world_shift
        self.display_surface.blit(self.background,(self.x,0))

    def __del__(self):
        print('level destoyed')

    def win_active(self):
        player = self.player.sprite
        win = self.win_block.sprite
        if player.rect.colliderect(win.rect):
            self.wine = True
            print('касаемся')
        else:
            self.wine = False
    def win_activated(self):
        keys = pygame.key.get_pressed()
        player = self.player.sprite
        if keys[pygame.K_e]:
            if self.wine and player.coinwallet == 3:
                self.win_act = True
                player.coinwallet -= 3
                self.win_block.sprite.kill()

    def win_end(self):
        if self.win_act:
            print(1)
            self.king = pygame.image.load('sprites\\win_block.png')
            self.display_surface.blit(self.king,(self.player.sprite.rect.topleft[0], self.player.sprite.rect.topleft[1] - 40))
            print(self.player.sprite.rect.topleft)
            self.winner = pygame.image.load('winner.png').convert_alpha()
            self.display_surface.blit(self.winner,(0,0))


    def score(self):
        self.font = pygame.font.Font(None, 75)
        self.score_text = self.font.render('Coins:',True, (255,255,0))
        self.score_text2 = self.font.render(str(self.player.sprite.coinwallet),True,(255,255,0))
        self.display_surface.blit(self.score_text,(0,0))
        self.display_surface.blit(self.score_text2,(165,0))

    def text_press_e(self):
        if self.richage:
            self.font1 = pygame.font.Font(None, 40)
            self.text = self.font1.render('press e',True,(255,255,255))
            self.display_surface.blit(self.text,(self.richag.sprite.rect.topleft[0],self.richag.sprite.rect.topleft[1] - 30))
        if len(self.win_block) == 1:
            if self.wine:
                self.font1 = pygame.font.Font(None, 40)
                self.text = self.font1.render('press e',True,(255,255,255))
                self.display_surface.blit(self.text,(self.win_block.sprite.rect.topleft[0],self.win_block.sprite.rect.topleft[1] - 30))





    def run(self):
        self.background_scroll()
        #монеты
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.coin_collision()
        #шипы
        self.spike_collision()
        self.spikes.update(self.world_shift)
        self.spikes.draw(self.display_surface)
        #плитка
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.doors.update(self.world_shift)
        self.doors.draw(self.display_surface)
        if len(self.doors) > 0:
            self.doors_open()
        #richag
        self.richag.update(self.world_shift)
        self.richag.draw(self.display_surface)
        if len(self.richag) == 1:
            self.richag_activated()
        self.richag_input()

        #поворотный блок
        self.turn_blocks.update(self.world_shift)

        # враги
        self.vrags.update(self.world_shift)
        self.vrags.draw(self.display_surface)
        self.vrag_collision()
        self.vrag_turn()

        #вин_блок
        self.win_block.update(self.world_shift)
        self.win_block.draw(self.display_surface)
        if len(self.win_block) == 1:
            self.win_active()
            self.win_activated()

        self.scroll_x()
        self.player.update()
        self.player.draw(self.display_surface)
        self.text_press_e()
        self.score()
        self.win_end()

        self.horizontal_movement_collision()
        self.vertical_movement_collision()



