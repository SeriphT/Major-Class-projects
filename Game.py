#Sabastian Taton
#Aug. 31
#Shmup


#imports
import pygame
import random
import os

#window
WIDTH = 480
HEIGHT = 600
FPS = 60

#defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#asset folder setup
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


#Sprites
class Player(pygame.sprite.Sprite):
 def __init__(self):
     pygame.sprite.Sprite.__init__(self)
     ## self.image = pygame.image.load(os.path.join(img_folder, "ship.png")).convert
    ##self.image.set_colorkey(BLACK)
    ##  self.image.fill(BLACK)
    ##  self.rect = self.image.get_rect()
    ##  self.rect.center = (WIDTH/2, HEIGHT/2)
    ##  self.y_speed = 5

#rectangle for testing purposes
     self.image = pygame.Surface((50,40))
     self.image.fill(GREEN)
     self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH/2
    self.rect.bottom = HEIGHT - 10
    self.speedx = 0
    
def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if  keystate[pygame.K_LEFT] :
               self.speedx = -5
        if  keystate[pygame.K_RIGHT] :
                self.speedx = 5
         self.rect.x = self.speedx
        if self.rect.right > WIDTH :
            self.rect.right = WIDTH
        if self.rect.left  < 0:
            self.rect.left = 0
         
#Pygame initialization and window setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,  HEIGHT))
pygame.display.set_caption("SHMUP!!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game loop
running = True
while  running:
    #keeps game running at right spped
    clock.tick(FPS)
        #Process input (events)
        for event in pygame.event.get():
                #check for window close
                if  event.type == pygame.QUIT:
                        running = False
                
        #Update
        all_sprites.update()
        
        #Render
        screen.fill(BLUE)
        all_sprites.draw(screen)
         #after drawing everything flip display
        pygame.display.flip()
        
        pygame.quit()
