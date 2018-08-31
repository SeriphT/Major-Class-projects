#Sabastian Taton
#Aug. 31
#Pygame Skeleton


#imports
import  pygame
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


#Pygame initialization and window setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,  HEIGHT))
pygame.display.set_caption("Game  Name")
clock = pygame.time.Clock()


#Game loop
running = True
while  running:
        #Process input
        for event in pygame.event.get():
                #check for window close
                if  event.type == pygame.QUIT:
                        running = False

        #Update


        #Render
        screen.fill(WHITE)
         #after drawing everything flip display
        pygame.display.flip()
        
