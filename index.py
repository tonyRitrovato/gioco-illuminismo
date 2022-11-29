import pygame

pygame.init()

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def draw():
    screen.fill((55,55,55))

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    update()
