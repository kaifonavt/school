import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Circle Follows Cursor")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.circle(screen, BLUE, (mouse_x, mouse_y), 25)


    pygame.display.flip()
