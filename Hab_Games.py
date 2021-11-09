import pygame
from Zmeika import Zmeika, close_game
from Arkanoid import Arcanoid
import csv

a = 0
b = 10


def Menu():
    def play():
        pygame.init()
        RES = 800  # Размер окна
        fps = 60
        Color = ['red', 'orange']
        x, y = 0, 0
        font_play = pygame.font.SysFont('Arial', 80, bold=True)  # размер текста
        displau = pygame.display.set_mode((RES, RES))
        Clock = pygame.time.Clock()
        img = pygame.image.load('Zadnuy_fon_na_vhod.jpg').convert()  # картинка
        while True:
            n = 1
            displau.blit(img, (0, 0))
            render_score = font_play.render(f'Играть', 1, pygame.Color(Color[n]))
            displau.blit(render_score, (100, 450))
            render_score2 = font_play.render(f'Выйти', 1, pygame.Color(Color[n]))
            displau.blit(render_score2, (500, 450))


            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > 100 and x < 200 and y > 450 and y < 500:
                    Zmeika()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > 500 and x < 600 and y > 450 and y < 500:
                    Menu()
                elif event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()
            Clock.tick(fps)

    def play2():
        pygame.init()
        RES = 800  # Размер окна
        fps = 60
        Color = ['red', 'orange']
        x, y = 0, 0
        font_play = pygame.font.SysFont('Arial', 80, bold=True)  # размер текста
        displau = pygame.display.set_mode((RES, RES))
        Clock = pygame.time.Clock()
        img = pygame.image.load('Zadnuy_fon_na_vhod.jpg').convert()  # картинка
        while True:
            n = 1
            displau.blit(img, (0, 0))
            render_score = font_play.render(f'Играть', 1, pygame.Color(Color[n]))
            displau.blit(render_score, (100, 450))
            render_score2 = font_play.render(f'Выйти', 1, pygame.Color(Color[n]))
            displau.blit(render_score2, (500, 450))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > 100 and x < 200 and y > 450 and y < 500:
                    Arcanoid()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > 500 and x < 600 and y > 450 and y < 500:
                    Menu()
                elif event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()
            Clock.tick(fps)
    WIDTH, HEIGHT = 1600, 900  # Размер окна


    fps = 1
    while True:
        x, y = 0, 0
        pygame.init()  # инициалезируем модули пайгейм
        Okno = pygame.display.set_mode(([WIDTH, HEIGHT]), pygame.FULLSCREEN)  # размер экрана
        clock = pygame.time.Clock()
        img = pygame.image.load('Menu.jpg').convert()
        Zmei = pygame.image.load('Zmeikas.jpg').convert()
        Ark = pygame.image.load('Arkanoid.jpg').convert()
        Exit = pygame.image.load('exit.jpg').convert()
        Okno.blit(img, (0, 0))
        Okno.blit(Zmei, (5, 5))
        Okno.blit(Ark, (210, 5))
        Okno.blit(Exit, (415, 5))
        close_game()
        pygame.display.flip()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > 5 and x < 205 and y > 5 and y < 205:
                play()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > 210 and x < 410 and y > 5 and y < 205:
                play2()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > 415 and x < 615 and y > 5 and y < 205:
                exit()
Menu()


