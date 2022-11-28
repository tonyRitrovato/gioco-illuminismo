import sys
import random
 
import pygame
from pygame.locals import *

class tubo:
  def __init__(self):
    self.x = 300
    self.y = random.randint(-75, 150)
  def avanza(self):
    self.x -= velocita
    screen.blit(tuboGiu, (self.x, self.y + 210))
    screen.blit(tuboSu, (self.x, self.y - 210))

def init():
  global rossx, rossy, rossVely
  global basex 
  global tubi
  rossx,rossy = 60,150
  rossVely = 0
  basex = 0
  tubi = []
  tubi.append(tubo())

def draw():
  screen.blit(sfondo, (0,0))
  for t in tubi:
    t.avanza()
  screen.blit(ross, (rossx, rossy))
  screen.blit(base, (basex,400))

def update():
  pygame.display.update()
  pygame.time.Clock().tick(fps)

def lose():
  screen.blit(gameOver, (50,180))
  update()
  restart = False
  while not restart:
     for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
          init()
          restart = True
        if event.type == pygame.QUIT:
          pygame.quit()

 
pygame.init()

sfondo = pygame.image.load('img/sfondo.png')
ross = pygame.image.load('img/uccello.png')
gameOver = pygame.image.load('img/gameover.png')
base = pygame.image.load('img/base.png')
tuboGiu = pygame.image.load('img/tubo.png')
tuboSu = pygame.transform.flip(tuboGiu, False, True)
 
width, height = 288,512
screen = pygame.display.set_mode((width, height))
fps = 60
velocita = 3

init()
 
# Game loop.
while True:
  if basex < -45:
    basex=0
  basex -= velocita
  rossVely += 1
  rossy += rossVely
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
      rossVely = -10
  if tubi[-1].x < 150:
    tubi.append(tubo())
    if event.type == pygame.QUIT:
      pygame.quit()
  if rossy > 380:
    lose()
  draw()
  update()