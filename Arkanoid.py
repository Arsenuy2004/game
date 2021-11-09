import pygame
from random import randrange as rnd  # Генератор диопазона случайных чисел



def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def Arcanoid():
    WIDTH, HEIGHT = 1200, 800
    fps = 60
    font_score = pygame.font.SysFont('Arial', 26, bold=True)  # размер текста
    paddle_w = 330  # ширина платформы
    paddle_h = 35  # ее высота
    paddle_speed = 15  # скорость платформы
    paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)  # платформа размещение
    # Настройки нара
    ball_radius = 20  # радиус шрика
    ball_speed = 6  # скорость шарика
    ball_rect = int(ball_radius * 2 ** 0.5)  # расетная величена
    ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)  # шар размещение
    dx, dy = 1, -1
    # Настройки блока
    block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
    color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]

    pygame.init()
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    # картинки
    img = pygame.image.load('Arkanoid2.jpg').convert()

    while True:
        sc.blit(img, (0, 0))
        render_score = font_score.render(f'Осталось кубиков: {len(block_list)}', 1, pygame.Color('orange'))
        sc.blit(render_score, (850, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
        pygame.draw.rect(sc, pygame.Color('darkorange'), paddle)  # платформа
        pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
        # настройка шара
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy

        if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
            dx = -dx

        if ball.centery < ball_radius:
            dy = -dy

        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)
            # if dx > 0:
            #     dx, dy = (-dx, -dy) if ball.centerx < paddle.centerx else (dx, -dy)
            # else:
            #     dx, dy = (-dx, -dy) if ball.centerx >= paddle.centerx else (dx, -dy)
        # смерть блока
        hit_index = ball.collidelist(block_list)
        if hit_index != -1:
            hit_rect = block_list.pop(hit_index)
            hit_color = color_list.pop(hit_index)
            dx, dy = detect_collision(dx, dy, ball, hit_rect)
            # постсмертный эффект
            hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
            pygame.draw.rect(sc, hit_color, hit_rect)
            fps += 2
        # победа или пройгрш
        if ball.bottom > HEIGHT:
            return
        elif not len(block_list):
            return
        # упровление
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0 or key[pygame.K_a] and paddle.left:
            paddle.left -= paddle_speed
        if key[pygame.K_RIGHT] and paddle.right < WIDTH or key[pygame.K_d] and paddle.right < WIDTH:
            paddle.right += paddle_speed

        pygame.display.flip()
        clock.tick(fps)
