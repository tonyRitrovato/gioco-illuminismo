import sys 
import pygame

def init():
    global adamx
    adamx = 160

def draw():
    screen.blit(earth, (0,0))
    screen.blit(adam, (adamx,520))
    
pygame.init()

bigAdam = pygame.image.load('img/adamSmith.PNG')
earth = pygame.image.load('img/earthBackground.jpg')
adam = pygame.transform.scale(bigAdam, (80,80))

height, width = 600,400
screen = pygame.display.set_mode((width, height))
fps = 60
init()
while True:
    
    mov = pygame.key.get_pressed()
    if mov[pygame.K_LEFT]:
        if adamx > 0:
            adamx -= 3
    if mov[pygame.K_RIGHT]: 
        if adamx < 320:
            adamx += 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(255, 255, 255),pygame.Rect(0, 80, 50, 10))
    draw()
    pygame.display.update()
    pygame.time.Clock().tick(fps)
pygame.quit()