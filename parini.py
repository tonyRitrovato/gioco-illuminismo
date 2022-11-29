import pygame
import os
    

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def draw():
    screen.fill((21,21,21))
    screen.blit(nobile, (0, nobileY))
    screen.blit(contadino, (720, contadinoY))
    palla = pygame.Rect(pallax,pallaY,20,20)
    pygame.draw.rect(screen, (255,255,255), palla)
    s_render = font.render(s, 1, (255,255,255))
    screen.blit(s_render, (0,0))

def init():
    global nobileY, contadinoY
    nobileY = 220
    contadinoY = 220
    global pallax, pallaY
    pallax = 380
    pallaY = 1

pygame.init()

init()

width, height = 800,600
imgHeight = 120
imgWidth = 80
screen = pygame.display.set_mode((width, height))
fps = 60
bigNobile = pygame.image.load('img/nobile.jfif')
bigContadino = pygame.image.load('img/contadino.jpg')
nobile = pygame.transform.scale(bigNobile, (imgWidth, imgHeight))
contadino = pygame.transform.scale(bigContadino, (imgWidth, imgHeight))
font = pygame.font.SysFont('Comic Sans MS', 12, bold=True)
global s 
s = 'il nobile e il contadino stanno litigando nella tomba, chi vincerà lo scontro?'
dx = 5
dy = 5

while True:

    pallax += dx
    pallaY += dy

    if pallaY > 580:
        pallaY=580
        dy *= -1
    
    elif pallaY  < 0:
        pallaY = 0
        dy *= -1

    if pallax  + 20 > 800:
        dx *= -1

    elif pallax < 0:
        dx *= -1

    if pallax < 80 and pallaY > nobileY and pallaY < nobileY + 120:
        dx *= -1 

    elif pallax > 700 and pallaY >  contadinoY and pallaY < contadinoY + 120:
        dx *= -1 
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    mov = pygame.key.get_pressed()
    if mov[pygame.K_w]:
        if nobileY > 0:
            nobileY -= 5
    if mov[pygame.K_s]: 
        if nobileY < 480:
            nobileY += 5
    if mov[pygame.K_UP]:
        if contadinoY > 0:
            contadinoY -= 5
    if mov[pygame.K_DOWN]: 
        if contadinoY < 480:
            contadinoY += 5
    draw()
    update()
