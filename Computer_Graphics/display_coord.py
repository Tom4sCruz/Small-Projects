import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Coordinates of cursor")

my_font = pygame.font.SysFont('Arial', 20)
running = True
clock = pygame.time.Clock()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    mouse_pos = pygame.mouse.get_pos()
    screen.fill((255,255,255))
    text_surface = my_font.render(f'({mouse_pos[0]}, {mouse_pos[1]})', False, (0,0,0))
    screen.blit(text_surface, (mouse_pos[0] + 10, mouse_pos[1] + 5))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
