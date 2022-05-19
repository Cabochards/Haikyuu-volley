import pygame 
import random

'''
class Terrain(object):
    
    nom = ""
    joueur_sur_terrain = []
    
    
    def __init__(self, name):
        self.name = name

    def joueurs_sur_terrain(self, player):
        self.joueur_sur_terrain.append(player)
    
    def display(self, scr):
        for player in self.joueur_sur_terrain:
            pygame.draw.circle(scr, player.equipe,(int(player.position[0]), int(player.position[1])), player.taille)
'''      
        

class Joueurs():
    

    

    def __init__(self):
        self.role = ""
        self.image = pygame.image.load("images/circle-icon-11.jpg")
        self.rect= self.image.get_rect()
        self.rect.x= 480
        self.rect.y= 345
    
    nombre = 7

    def Apparait(self):
        
        positions = [  (480,345), (140,450),(20,362),(280,370),(710,410) ] #on definit une liste de positions
        self.image= pygame.image.load("images/circle-icon-11.jpg") #taupe 1 hit qui apparait a un lieu de base
        nid= positions[1]
        self.rect.x= nid[0]  
        self.rect.y= nid[1]
      





pygame.init()

vitesse=pygame.time.Clock()#pour les fps
#creation de la taille de la fenetre 

screen=pygame.display.set_mode((1000,700))
pygame.display.set_caption('Chasse-taupe')


Icone = pygame.image.load('images/ball.jpg')
pygame.display.set_icon(Icone)

background= pygame.image.load('images/bg.jpg')
background_rect= background.get_rect()

Sur_le_terrain = []

for i in range(Joueurs.nombre):
    Players= Joueurs()
    Sur_le_terrain.append(Players)

keep = True
while keep:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep = False
    
        
    screen.blit(background,(0,0))

   
    pygame.display.update()
    vitesse.tick(200)

pygame.quit()