import pygame, sys
from pygame.color import THECOLORS
from pygame import font
pygame.init()
def myhelp():
    pygame.display.set_caption("Крутая игра")
    screen = pygame.display.set_mode([600, 600])
    background = pygame.Surface(screen.get_size())
    background.fill([0, 0, 0])
    color = THECOLORS["white"]
    top = 10
    left = 20
    font = pygame.font.Font(None, 20)
    my_file = open('helpgame.txt', 'r')  # Открываем файл для чтения
    lines = my_file.readlines()  # Записываем строки из файла в список lines
    my_file.close()
    dlina = len(lines)  # Это количество строк
    for i in range(0, dlina):
        ln = lines[i]
        dl = len(ln) - 1  # Удаляем символ конца строки
        ln = ln[0:dl]  # Копируем из исходной строки все, кроме символа конца строки
        text = font.render(ln, 1, color)
        background.blit(text, [left, top])
        top = top + 20  # Следующая строка выводится ниже на 20 пикселей
        text = font.render("Press any key", True, color)
        background.blit(text, [150, 550])
        screen.blit(background, (0, 0))
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    running = False
                    print(1)



