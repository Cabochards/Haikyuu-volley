import pygame
from pygame.draw import rect
from pygame.sprite import collide_rect
import Volley_class
from pygame.display import set_icon


pygame.init()

vitesse=pygame.time.Clock()#pour les fps
#creation de la taille de la fenetre 

screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption('Tableau de volley')


Icone = pygame.image.load('images/ball.jpg')
pygame.display.set_icon(Icone)

background= pygame.image.load('images/bg.jpg')
background_rect= background.get_rect()





running= True
 
while running :
    
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False # running est sur False
        if event.type==pygame.QUIT:
           running = False
        
      
        
    
    pygame.display.flip()
   

pygame.quit()  