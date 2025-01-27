import pygame

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Body with Trace")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

RADIUS = 3

background = pygame.Surface(screen.get_size())
background.fill(WHITE)

running = True
while running:
    screen.blit(background, (0, 0))  # Keep previous drawings

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw moving circle
    mx, my = pygame.mouse.get_pos()
    pygame.draw.circle(background, BLUE, (mx, my), RADIUS)

    pygame.display.flip()

pygame.quit()