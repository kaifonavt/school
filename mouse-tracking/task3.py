import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Drag and Drop")

BLACK = (0, 0, 0)
RED = (255, 0, 0)

square_size = 50
square_x, square_y = 275, 175
dragging = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if square_x <= mouse_x <= square_x + square_size and square_y <= mouse_y <= square_y + square_size:
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                square_x = mouse_x - square_size // 2
                square_y = mouse_y - square_size // 2
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    pygame.display.flip()
