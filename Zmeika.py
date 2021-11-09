import pygame
from random import randrange
import csv

RES = 800  # Размер окна
SIZE = 50  # Размер чанка

def close_game():  # проверка событий на закрытие приложения
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def Zmeika():
    pygame.init()  # инициалезируем модули пайгейм
    surface = pygame.display.set_mode([RES, RES])  # размер экрана
    clock = pygame.time.Clock()  # регулируем скорость змейки
    font_score = pygame.font.SysFont('Arial', 26, bold=True)  # размер текста
    font_end = pygame.font.SysFont('Arial', 66, bold=True)  # размер текста
    img = pygame.image.load('Fon_zmeika.jpg').convert()  # картинка
    img2 = pygame.image.load('3.png').convert()
    img3 = pygame.image.load('Tulovische.jpg').convert()
    Hvost = pygame.image.load('Xvost.jpg').convert()
    Mysh = pygame.image.load('Mysh.jpg').convert()
    x, y = randrange(SIZE, RES - SIZE * 3, SIZE), randrange(SIZE, RES - SIZE * 3, SIZE)  # спавн змейуи
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # спавн яблока
    x1, y1 = apple
    length = 1  # размер змейки
    snake = [(x, y)]  # змейка
    dx, dy = 0, 0  # направление движения
    fps = 60  # скорость змейки
    dirs = {'W': True, 'S': True, 'A': True, 'D': True, }  # словарь
    speed_count, snake_speed = 0, 10

    score = 0
    score2 = 0
    # if score > score2:
    score = score

    while True:

        surface.blit(img, (0, 0))
        [surface.blit(img3, (i, j)) for i, j in snake]  # закраска всех элементов змейки в картинку
        surface.blit(Mysh, (*apple, SIZE, SIZE))  # закраска всех яблок в красный
        surface.blit(Hvost, snake[0])
        surface.blit(img2, snake[-1])





        render_score = font_score.render(f'Очки: {score}', 1, pygame.Color('orange'))
        surface.blit(render_score, (5, 5))
        # snake movement
        speed_count += 1
        if not speed_count % snake_speed:
            x += dx * SIZE  # шаг змейки по x
            y += dy * SIZE  # шаг змейки по y
            snake.append((x, y))  # добовление координат змейки в список
            snake = snake[-length:]  # срез необходимого размера змейки
        # eating food
        if snake[-1] == apple or apple in snake:  # когда последний элемент равен положению яблока мы его сьели
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # спавним новое яблоко

            length += 1  # прибовляем змейке длину
            score += 1
            snake_speed -= 1
            snake_speed = max(snake_speed, 4)
        # Случаи пройгрыша
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):  # если мы вышли за экран или сьели себя пройгрыш и активация цикла нижк
            while True:
                render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))  # надпись
                surface.blit(render_end, (RES // 2 - 200, RES // 3))  # спавн надписи
                pygame.display.flip()
                return



        pygame.display.flip()  # обновление поверхности каждую итерацию
        clock.tick(fps)  # задержка
        close_game()
        # упровление
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True, }  # проверка на нажимаемую кнопку
        elif key[pygame.K_s]:
            if dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
        elif key[pygame.K_a]:
            if dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
        elif key[pygame.K_d] :
            if dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True, }

