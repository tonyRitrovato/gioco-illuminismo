import pygame
import os

pygame.init()

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def draw():
    screen.fill((21,21,21))
    pygame.draw.rect(screen, (55,55,55), rousseau)
    pygame.draw.rect(screen, (55,55,55), adam)
    pygame.draw.rect(screen, (55,55,55), parini)
    pygame.draw.rect(screen, (55,55,55), beccaria)
    sr_render = font.render(sr, 1, (255,255,255))
    screen.blit(sr_render, (60,75))
    sa_render = font.render(sa, 1, (255,255,255))
    screen.blit(sa_render, (410,75))
    sp_render = font.render(sp, 1, (255,255,255))
    screen.blit(sp_render, (60,205))
    sb_render = font.render(sb, 1, (255,255,255))
    screen.blit(sb_render, (410,205))

width, height = 600, 350
screen = pygame.display.set_mode((width, height))
rectX, rectY = 150, 90
rousseau = pygame.Rect(50,50 ,rectX, rectY)
adam = pygame.Rect(400, 50, rectX, rectY)
parini = pygame.Rect(50, 180, rectX, rectY)
beccaria = pygame.Rect(400, 180, rectX, rectY)
font = pygame.font.SysFont('Comic Sans MS', 20, bold=True)
sr = 'Rousseau'
sa = 'Adam Smith'
sp = 'Parini'
sb = 'Beccaria'
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    focus = pygame.mouse.get_focused
    pos = pygame.mouse.get_pos
    if focus and pygame.mouse.get_pressed()[0]:
        if pos()[0] > 50 and pos()[0] < 200 and pos()[1] > 50 and pos()[1] < 140:
            os.system('python Rousseau.py')
        if pos()[0] > 400 and pos()[0] < 550 and pos()[1] > 50 and pos()[1] < 140:
            os.system('python adamSmith.py')
        if pos()[0] > 50 and pos()[0] < 200 and pos()[1] > 180 and pos()[1] < 270:
            os.system('python parini.py')
        if pos()[0] > 400 and pos()[0] < 550 and pos()[1] > 180 and pos()[1] < 270:
            os.system('python beccaria.py')  
    draw()
    update()
