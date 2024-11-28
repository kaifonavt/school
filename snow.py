import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Падающий 1  снег")

# Цвет снежинок
white = (255, 255, 255)

# Список для хранения снежинок (каждая снежинка - это список [x, y, размер])
snowflakes = []

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполняем экран черным цветом
    screen.fill((0, 0, 0))

    # Создаем новые снежинки
    for _ in range(10):
        snowflakes.append([random.randint(0, screen_width), random.randint(-20, -10), random.randint(2, 5)])

    # Обновляем и рисуем снежинки
    for snowflake in snowflakes:
        # Двигаем снежинку вниз
        snowflake[1] += 1

        # Если снежинка достигла нижней границы, переносим ее наверх
        if snowflake[1] > screen_height:
            snowflake[0] = random.randint(0, screen_width)
            snowflake[1] = random.randint(-20, -10)

        # Рисуем снежинку (круг)
        pygame.draw.circle(screen, white, (snowflake[0], snowflake[1]), snowflake[2])

    # Обновляем экран
    pygame.display.flip()

pygame.quit()
