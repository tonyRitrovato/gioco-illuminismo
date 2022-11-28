import sys
import random
 
import pygame
from pygame.locals import *

def init():
  global rossx, rossy, rossVely
  rossx,rossy = 60,150
  rossVely = 0

def draw():
  screen.blit(sfondo, (0,0))
  screen.blit(ross, (rossx, rossy))

def update():
  pygame.display.update()
  pygame.time.Clock().tick(fps)
 
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

init()
 
# Game loop.
while True:
  rossVely += 1
  rossy += rossVely
  draw()
  update()
  
