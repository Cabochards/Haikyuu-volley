import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def creer_terrain():
    """
    On cree un terrain rectangle avec:
    -La ligne de service
    -Les lignes d attaques dans les quelles liberos ne peuvent pas attaquer
    """
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)

    plt.plot([0,0],[0,90], color="black")
    plt.plot([0,130],[90,90], color="black")
    plt.plot([130,130],[90,0], color="black")
    plt.plot([130,0],[0,0], color="black")
    plt.plot([65,65],[0,90], color="pink")
    plt.plot([45,45],[0,90], color="red")
    plt.plot([85,85],[0,90], color="red")
    plt.show()

creer_terrain()


"""
class libero():
    
    def reception{}:
    def passe():
        
class joueur():
   
    def reception{}:
    def passe():
    def attaque():
    def smash()
"""