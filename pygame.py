import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Задаем размеры экрана
width = 600
height = 400

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Устанавливаем размер экрана
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Устанавливаем параметры игры
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения счета
def Your_score(score):
    value = score_font.render("Счет: " + str(score), True, black)
    screen.blit(value, [0, 0])

# Функция для отображения текста
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Функция для отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Главная функция игры
def gameLoop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = width / 2
    y1 = height / 2

    # Начальная скорость змейки
    x1_change = 0
    y1_change = 0

    # Список для хранения координат тела змейки
    snake_List = []
    Length_of_snake = 1

    # Позиция еды
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Цикл игры
    while not game_over:

        while game_close:
            screen.fill(blue)
            message("Ты проиграл! Нажми C для продолжения или Q для выхода", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка, не выходит ли змейка за границы
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)

        # Отрисовываем еду
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Обновляем тело змейки
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка, не столкнулась ли змейка сама с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Отрисовываем змейку
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Проверка на съеденную еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()
