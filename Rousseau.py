import sys
import random
 
import pygame
from pygame.locals import *

def init():
  global rossx, rossy, rossVely
  global basex 
  rossx,rossy = 60,150
  rossVely = 0
  basex = 0

def draw():
  screen.blit(sfondo, (0,0))
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
    if event.type == pygame.QUIT:
      pygame.quit()
  if rossy > 380:
    lose()
  draw()
  update()