import pygame

# Инициализация Pygame
pygame.init()

# Создаем окно
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Флаг Японии")

# Создаем первую поверхность (фон)
background = pygame.Surface((600, 400))
background.fill((0, 0, 100))  # Заполняем фоном синего цвета

# Создаем вторую поверхность (флаг)
flag = pygame.Surface((200, 100))
flag.fill((255, 255, 255))  # Белый фон
pygame.draw.circle(flag, (255, 0, 0), (100, 50), 40)  # Красный круг

# Бесконечный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка
    screen.blit(background, (0, 0))
    screen.blit(flag, (200, 150))  # Позиционируем флаг в центре экрана
    pygame.display.flip()

pygame.quit()
