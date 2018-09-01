#Sabastian Taton
#Aug. 31
#Starting a Game


#imports
import pygame
import random


#window
WIDTH = 360
HEIGHT = 480
FPS = 30

#defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#player Sprite
class Player(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.Surface((50, 50))
  self.image.fill(BLACK)
  self.rect = self.image.get_rect()
  self.rect.center = (WIDTH/2, HEIGHT/2)
  
  
#Pygame initialization and window setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,  HEIGHT))
pygame.display.set_caption("Game  Name")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_sprites.add(Player)
#Game loop
running = True
while  running:
        #Process input
        for event in pygame.event.get():
                #check for window close
                if  event.type == pygame.QUIT:
                        running = False

        #Update
        all_sprites.update()

        #Render
        screen.fill(WHITE)
        all_sprites.draw(screen)
         #after drawing everything flip display
        pygame.display.flip()
        
        pygame.quit()
