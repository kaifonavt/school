import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Draw Circle at Mouse Pointer")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw a red circle at mouse pointer
    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 25)

    # Update the display
    pygame.display.flip()
