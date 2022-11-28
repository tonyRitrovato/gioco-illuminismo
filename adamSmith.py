
import pygame
import random
class nemico:
    def __init__(self):
        nemico.x = random.randint(0,360)
        nemico.y = 0
    
    def avanza(self):
        self.y += 5
        screen.blit(stato, (self.x, self.y))
    
    def collisione(self, proiettili):
        for p in proiettili:
            tolleranza = 5
            pLatoDx = p.x + 40 - tolleranza
            pLatoSx = p.x + tolleranza
            nemicoLatoDx = self.x + 40
            nemicoLatoSx = self.x
            pLatoSu = p.y + tolleranza
            nemicoLatoGiu = self.y + 40
            #if pLatoDx > nemicoLatoSx and pLatoSx < nemicoLatoDx:
            if pLatoSu > nemicoLatoGiu and  pLatoDx > nemicoLatoSx and pLatoSx < nemicoLatoDx: 
                self.y = -50


        
class proiettile:
    def __init__(self):
        proiettile.x = adamx + 40
        proiettile.y = 520

    def avanza(self):
        self.y -= 8
        screen.blit(proiettileImg, (self.x, self.y))
        
def init():
    global adamx
    adamx = 160
    nemici.append(nemico())
    proiettili.append(proiettile())
    global s 
    s = 'aiuta Adam Smith ad evitare che lo stato interferisca nell\'economia'

def draw():
    screen.blit(earth, (0,0))
    screen.blit(adam, (adamx,520))
    for n in nemici:
        n.avanza()
    for p in proiettili:
        p.avanza()
    s_render = font.render(s, 1, (255,255,255))
    screen.blit(s_render, (0,0))
    
pygame.init()

bigAdam = pygame.image.load('img/adamSmith.PNG')
bigEarth = pygame.image.load('img/earthBackground.jpg')
earth = pygame.transform.scale(bigEarth, (400,600))
adam = pygame.transform.scale(bigAdam, (80,80))
bigStato = pygame.image.load('img/stato.jfif')
stato = pygame.transform.scale(bigStato, (40,40))
BigProiettileImg = pygame.image.load('img/proiettile.jpg')
proiettileImg = pygame.transform.scale(BigProiettileImg, (40,40))
font = pygame.font.SysFont('Comic Sans MS', 12, bold=True)

nemici = []

proiettili = []

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

       # if event.type == pygame.KEYDOWN and pygame.key == pygame.K_a:
    if mov[pygame.K_a] and proiettili[-1].y < 0: 
        proiettili.append(proiettile())
    
    if nemici[-1].y > 600 or nemici[-1].y < -40:
        nemici.append(nemico())
    for n in nemici:
        n.collisione(proiettili)
    draw()
    pygame.display.update()
    pygame.time.Clock().tick(fps)
pygame.quit()