import pygame
import random

"""""
class terrain():
    
    
    On cree un terrain rectangle avec:
    -La ligne de service
    -Les lignes d attaques dans les quelles liberos ne peuvent pas attaquer
    
    def zone_gauche():
        self.x=0
        self.y=0 
"""

class libero():
    """
    On cree une classe pour le libero :
    -Sa position initiale des le debut du match
    -Il peut se faire remplacer par le middle blocker
    -Il ne peut pas faire de coup offensif dans la zone d'attaque
    -Il ne peut pas bloquer, sevir et smasher
    """
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\libero_camp1.png")
        self.rect= self.image.get_rect()
        self.rect.x= 480
        self.rect.y= 345
    
    def reception(self,ball):
        """
        """
    
    def passe(self,ball):
        """
        """
class libero2():
    
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\libero_camp2.png")
        self.rect= self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 345
        
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """

class middble_blocker():

    """
     On cree une classe pour le middle blocher :
    -Sa position initiale des le debut du match
    -Il peut se faire remplacer par le libero
    -Il peut faire des coup offensif dans la zone d'attaque
    -Il peut bloquer, receptionner, passer servir et smasher
    """
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """

class middble_blocker2():
    
    """
     On cree une classe pour le middle blocher :
    -Sa position initiale des le debut du match
    -Il peut se faire remplacer par le libero
    -Il peut faire des coup offensif dans la zone d'attaque
    -Il peut bloquer, receptionner, passer servir et smasher
    """
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """

class setter():
    
    """
     On cree une classe pour le passeur :
    -Sa position initiale des le debut du match
    -Il peut faire des coup offensif dans la zone d'attaque
    -Il peut bloquer, receptionner, passer servir et smasher
    """
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """

class setter2():
    

    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """
    


class wingspiker():
    
    """
     On cree une classe pour les ailiers:
    -Sa position initiale des le debut du match
    -Il peut faire des coup offensif dans la zone d'attaque
    -Il peut bloquer, receptionner, passer servir et smasher
    """
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """

class wingspiker2():
    
    """
     On cree une classe pour les ailiers:
    -Sa position initiale des le debut du match
    -Il peut faire des coup offensif dans la zone d'attaque
    -Il peut bloquer, receptionner, passer servir et smasher
    """
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """

class oh():
    
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """

class oh2():
    
    def __init__(self):
        
        self.touche = 0
        self.image = pygame.image.load("images\player_camp1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 45
    
    def reception(self,ball):
        """
        """
    def passe(self,ball):
        """
        """
    def attaque(self,ball):
        """
        """
    def smash(self,ball):
        """
        """


class balle():
    
    def __init__(self) :
        
        self.rect= self.image.get_rect()
        self.rect.x= 480
        self.rect.y= 345
        self.image= pygame.image.load("images/ball.jpg")
      
    def possesion():
        """
        """