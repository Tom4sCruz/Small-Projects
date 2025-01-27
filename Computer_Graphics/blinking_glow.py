# The particle is small for the effect to become more plausible

import pygame
import time
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption("Blinking Red Circle with Glow")

# Colors
BLACK = (0, 0, 0)
ON_RED = (237,29,36)
OFF_RED = (100, 0, 0)
RED_GLOW = (60,20,20)

# [on_color, off_color, glow_color]
REDS = [ON_RED, OFF_RED, RED_GLOW]

# Circle properties
circle_pos = (WIDTH // 2, HEIGHT // 2)
radius = 5

class Particle:
    def __init__(self, colors):
        self.colors = colors
        self.glow = False

    def circle_surf(self, r, color):
        surf = pygame.Surface((r*2, r*2))
        pygame.draw.circle(surf, color, (r, r), r)
        surf.set_colorkey((0,0,0))
        return surf
    
    def glowing(self):
        if self.glow:
            pygame.draw.circle(screen, self.colors[0], circle_pos, radius)
            screen.blit(self.circle_surf(radius*2, self.colors[2]), (circle_pos[0] - radius*2, circle_pos[1] - radius*2), special_flags=BLEND_RGB_ADD)
        else:
            pygame.draw.circle(screen, self.colors[1], circle_pos, radius)

    def blink(self):
        self.glow = False if self.glow else True

    def update(self):
        self.glowing()
        self.blink()


running = True
visible = True  # Toggle visibility
clock = pygame.time.Clock()

particle = Particle(REDS)

while running:
    screen.fill(BLACK)  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    particle.update()
    time.sleep(0.5)

    pygame.display.flip()
    clock.tick(60)
    #time.sleep(0.5)  # Delay for blinking
    #visible = not visible  # Switch visibility

pygame.quit()

