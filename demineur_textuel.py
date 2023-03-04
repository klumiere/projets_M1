## Projet démineur Kamély LUMIERE 20190541 M1 GENIOMHE (fait seule)
##version textuelle##

import random
from copy import deepcopy #pour créer des copies de grilles

#on définit les noms de colonnes (en lettres) et le nom des lignes (en chiffres)

lignes=[" "," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
colonnes=[" "," A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


#fonction permettant d'afficher le contenu de la grille qui est une liste de liste sous forme de grille
def affiche_grille(g):
 #affichage de la grille
    for i in range(len(g)): #lignes 0 à 7 (=8 lignes)
        for j in range(len(g[i])): #colonnes 0 à 16 (=17 lignes)
            print(g[i][j], end=" ")
        print()
        
        
        

def creer_grille_ini_joueur(l,c):
     #grille avec des cases vides initialement
    
    grille=[[ "-" for j in range(c+1)] for i in range(l+1)] #+1 pour avoir la case (0,0) vide et avoir une "belle" grille
    #print(grille)
    
    
    grille[0][0]=" "
    
    #mets des chiffres pour le nom des lignes
    i=1
    while(i<len(grille)):
        grille[i][0]=lignes[i]
        
        i+=1
        
    #mets des lettres pour le nom des colonnes   
    j=1
    
    while(j<len(grille[i-1])):
        grille[0][j]=colonnes[j]
        j+=1
     
     #mets des # au niveau de la bordure de la grille: 1ere et dernière ligne
    for i in (range(1, len(grille[l]))):
        
        grille[1][i]="#"
        grille[l][i]="#"
        
    #mets des # au niveau de la bordure de la grille: 1ere et dernière colonne
    for j in (range(1, len(grille))):
        
        grille[j][1]="#"
        grille[j][c]="#"
    
    global grille_ini
    grille_ini=deepcopy(grille)
    
    global grid
    grid=deepcopy(grille)
    
    
    print("Grille initiale:")
    print()
    affiche_grille(grille)
    
    

#fonction permettant de créer une grille avec l lignes, c+ col et placant k mines de manière aléatoire dans la grille
def remplir_creation_grille(l,c,m):

    creer_grille_ini_joueur(l,c)
    
    #disposition aléatoire des k mines représenté par "9" dans la grille
    
    #les bordures n'ont pas de mines
    
     #mets des 0 à la 1ère et dern lignes
    for i in (range(1, len(grille_ini[l]))):
        
        grid[1][i]=0
        grid[l][i]=0
        
    #mets des 0 à la 1ère et dern colonne
    for j in (range(1, len(grille_ini))):
        
        grid[j][1]=0
        grid[j][c]=0
        
    
        
     
        
    #on remplit les cases restantes avec mines "9" ou pas mines "0"
    mines=[]
    #permet de remplir la liste mines[] avec m mines représenté par 9 et le reste (càd c*l-m) par des 0
    for i in range(1,m+1):
        mines.append(9)
    
    for j in range(l*c-(2*c+2*l-4)-m): #on rajoute des 0 sur les restant des cases (en enlevant les cases de la bordure)
        mines.append(0)
    
    #print(mines)
    #comme les 9 sont tous dans les première postions de la liste on mélange avec la fonction shuffle
    random.shuffle(mines)
    #print()
    #print(mines)
    
    
   
    h=0

    while( h<len(mines)):

        for i in range(2,len(grid)-1):
            for j in range(2,len(grid[i])-1):
                grid[i][j]=mines[h]
                h+=1
        
    
    
    global grille_remplie
    grille_remplie=deepcopy(grid) #on copie les valeurs de grille dans une nouvelle grille qu'on appelle grille_remplie et on la mets en global pour l'utiliser dans la fonction mines_adj
    
    #print()
    #print("Grille remplie avec mines affichées:")
    #print()
    #affiche_grille(grille_remplie)
   


def grille_complete(l,c,m):
     
    remplir_creation_grille(l,c,m)
    
    global grille_mines_adj
    grille_mines_adj=deepcopy(grille_ini)
    
   
    for i in range(1,len(grille_ini)):
        for j in range(1,len(grille_ini[i])):
            if((i>=2) and (i<len(grille_ini)-1) and (j>=2) and(j<len(grille_ini[i])-1) ):
                grille_mines_adj[i][j]=(grille_remplie[i][j-1]+grille_remplie[i-1][j-1]+grille_remplie[i-1][j]+grille_remplie[i-1][j+1]+grille_remplie[i][j+1]+grille_remplie[i+1][j+1]+grille_remplie[i+1][j]+grille_remplie[i+1][j-1])//9
     
            else:
                grille_mines_adj[i][j]="B" #B=bord de la grille du démineur
            
    print()
    print("Grille avec les mines voisines:")
    print()            
    affiche_grille(grille_mines_adj)
      


def questions(l,c):

 
    print()
    print("Veuillez choisir une case:")
    global col
    global li
    
    #demande à l'utilisateur de saisir à nouveau une lettre tant que la valeur saisie n'est pas une lettre        
    while True:
    
        
        col=input("Saisir la colonne de la case choisie:")
        if(col.isdigit()==False and col.upper() in colonnes[1:len(colonnes)] and col.upper() != colonnes[1] and col.upper() != colonnes[c] ): #si ce n'est pas un nombre ET que après avoir mis en majuscule c'est dans la liste des lettres mais que c'est pas dans la bordure, l'utilisateur a bien saisi une lettre
            col=col.upper()
            if(col in colonnes[1:c+1]): #vérifie que l'utilisateur n'a pas saisit une lettre de colonne absente dans la grille
                break
                
                
    while True:
        li=input("Saisir la ligne de la case choisie:")
        if (li.isdigit()):
            li=int(li)
            if(li<l and li not in[0,1] ): #il faut que le n° de la ligne saisie soit présente dans la grille mais pas etre dans la bordure
                break
    
           
    
    
    
    #affiche la case choisie par le joueur
    #print("La case choisie est:",col+str(li),".")
    
    
    #col est un str donc faut trouver son indice en entier
    i=0
    while(col!=colonnes[i]):
        i+=1
        
    
    col=i #converti la colonne qui était en str sous forme d'une lettre en maj en entier par son indice dans la liste colonnes
    
    

    
###
   
def jeu_complet():
    
    #Demande à l'utilisateur de saisir à nouveau un entier tant que la valeur saisie n'est pas un entier pour le nombre de lignes+colonne avec la fonction isdigit() qui retourne vrai si la variable n'est csté que de chiffres 
    
    
      
    while True:
        l=input("Saisir le nombre de lignes de la grille:")
        if (l.isdigit()):
            l=int(l)  #permet de convertir l,c et m qui étaient des str en int pour les utiliser dans la fonction grille_complète
    
            if(l<=26): #ne créer pas de grille plus grande que la dimension 26x26
                break
                
    
    
            
           
    while True:
        c=input("Saisir le nombre de colonnes de la grille:")
        if (c.isdigit()):
            c=int(c)
            if (c<=26):
                break
    
    while True:
        m=input("Saisir le nombre de mines dans la grille:")
        if(m.isdigit()):
            m=int(m)
            if(m>0 and l*c-(2*c+2*l-4)-m>0 ):
            #if (m<l*c-10): #il faut qu'il y ai pas plus de mines que le nb total de cases et que toutes les cases soient pas minées
                break
    print()
    print("Dimension grille: ", l, "x",c, " avec ", m, " mines.")
    print()
    global r #variable r indiquant le nb de cases retstant à déminer
    r=l*c-m

    #screer_grille_ini_joueur(l,c)   
    
    
   
    remplir_creation_grille(l,c,m)
    
    questions(l,c)
    
    #complète au fur et à mesure le nb de mines adj quand la case choisie n'est pas minée
    grille_complete(l,c,m)
    while(grille_remplie[li][col]!=9):
        
        grille_ini[li][col]=grille_mines_adj[li][col]
        affiche_grille(grille_ini)
        questions(l,c)
    print()
    print("PERDU!")
    print()
    affiche_grille(grille_remplie)
    
        

        
        
 
    
    
    
    
###programme principal

jeu_complet()

    
    
    
    


