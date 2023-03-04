## Projet démineur Kamély LUMIERE 
##programme avec l'affiche de la grille initiale uniquement###

from tkinter import *
import tkinter
import tkinter.font as tkFont #pour la police des textes
from tkinter import messagebox
from tkinter import Menu, LabelFrame, IntVar,StringVar,  Label


#on définit les noms de colonnes (en lettres) et le nom des lignes (en chiffres) pour constuire la grille du démneur
lignes=[" "," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
colonnes=[" "," A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]



#couleur des bg et fg pour les boutons
lavande="#EA3FF7"
bleu="#0023F5"


class Page:
    
    def __init__(self):
    
        self.fen=tkinter.Tk()
        self.titre="Nouvelle Page"
        self.fen.title(self.titre)
        self.fen.geometry("500x600")
        
        

###4###
class Page_grille_ini(Page):

    def __init__(self):
        Page.__init__(self)
        self.titre="Nouvelle Partie: Grille initiale" #pour une page_nom le titre de la fen est modifié
        self.fen.title(self.titre)  
       
        
          
          
               
        
        
##classes pour afficher les éléments du jeu de démineur

class Case:

    #attributs d'instance
    pgi=Page_grille_ini().fen
    val_case_def="-"  #valeur des cases de la grille par défaut

    #constructeur
    def __init__(self,ligne,colonne):
        
        self.__ligne=ligne
        self.__colonne=colonne
        #print('nelle case')
        #print("Nelle case de coordonnée: ", ligne, ",",colonne)
        #print(self.valeur)
       
        self.bouton=tkinter.Button(Case.pgi,text=Case.val_case_def, width=1, height=1, bg=lavande,fg=bleu)
        self.bouton.grid(row=self.__ligne, column=self.__colonne)
        
        
        
    #méthodes
    #récupère la ligne de la case
    def getLigne(self):
        return(self.__ligne)
        
    #récupère la colonne de la case    
    def getCol(self):
        return(self.__colonne)
    
    
    #récupère la valeur du bouton d'une case
    def getVal(self):
        return(self.valeur) 
            
    #change la valeur du boutton d'une case
    def setVal(self,nelle_val):
        self.valeur=nelle_val
        self.bouton=tkinter.Button(Case.pgi,text=self.valeur, width=1, height=1, bg="#F241FF",fg="#0013C2")
        self.bouton.grid(row=self.__ligne, column=self.__colonne)
    
        
    #change la couleur du boutton d'une case
    def setColorBG(self,nelle_couleur_bg):
        self.couleur_bg=nelle_couleur_bg
        self.bouton=tkinter.Button(Case.pgi,text=Case.val_case_def, width=1, height=1, bg=self.couleur_bg,fg=bleu)
        self.bouton.grid(row=self.__ligne, column=self.__colonne)
    
        
    
    #change la couleur du texte du boutton d'une case
    def setColorFG(self,nelle_couleur_fg):
        self.couleur_fg=nelle_couleur_fg
        self.bouton=tkinter.Button(Case.pgi,text=Case.val_case_def, width=1, height=1, bg=lavande,fg=self.couleur_fg)
        self.bouton.grid(row=self.__ligne, column=self.__colonne)
        


        
     
class Grille:

    #constructeur
    def __init__(self,nb_l,nb_col):
        self.__nb_l=nb_l
        self.__nb_col=nb_col
        self.grille=[[]]
        print("Je suis une nelle grille de dimension ", nb_l , "X", nb_col)
        
        
        self.grille=[[Case(i,j) for j in range(0,self.__nb_col+1)] for i in range(0,self.__nb_l+1)]
       
        Case(0,0).setVal(" ")
        Case(0,0).setColorBG("#0013C2")
        
        #mets des chiffres pour le nom des lignes
        i=1
        while(i<len(self.grille)):
            
            Case(i,0).setVal(lignes[i])
            i+=1
        
        #mets des lettres pour le nom des colonnes   
        j=1
        while(j<len(self.grille[i-1])):
            
            Case(0,j).setVal(colonnes[j])
            j+=1
            
            
            
    def questions(self):
        tkinter.messagebox.askquestion(title="Question", message="Choisir une case qui ne soit pas dans les bordures")
        
        
class Grille_rep(Grille):
    def __init__(self):
    
        Grille.__init__(self)
        self.mines=[]
        global grid
        self.grid=deepcopy(grille)
        
        
        

     
        

        
        
      
   
        

############ Remarques##############
    ## Je n'ai pas réussi à afficher la grille en fonction de la dimension saisi par l'utilisateur, mais si on saisi nous même le nb de ligne/col il y a un affichage, mais "c'est pas relié au reste de l'IG"...
    ### Avec ce soucis, je n'ai pas pu faire les grilles du jeu du démineur...###


        
  
     
########################     	     
 
###3bis###
class Page_niv_perso(Page): #permet de générer une page pour saisir sois même le nb de ligne et colonnes

    def __init__(self):
    
        Page.__init__(self)
        self.titre="Niveau personnalisé" #pour une Page_niv_perso le titre de la fen est modifié
        self.fen.title(self.titre) 
        
        self.nb_col=0
        self.nb_l=0 
          
        label = Label( self.fen, text="Saisir le nb de lignes de la grille:")
        label.pack()
        
        ## dim_lignes
        #1/ zone pour saisir un entier pour le nb de lignes
        self.__nb_lignes=IntVar()
        
        nbl = Entry(self.fen, textvariable=self.__nb_lignes )
        nbl.focus_set()
        nbl.pack()
        
        #bouton Valider
        bv1 = Button(self.fen, text="Valider",command=self.dim_col)
        bv1.pack()
        
    def dim_col(self):
        
        #2/ Après validation, vérifie la valeur du nb de lignes saisie
        #si la valeur est correcte on passe à la suite
        print(type(self.__nb_lignes.get()))
        if(self.__nb_lignes.get()<=26 and self.__nb_lignes.get()!=0):
            #créer zone pour saisir le nb de col
            self.__nb_col=IntVar()
            label= Label (self.fen, text="Saisir le nombre de colonnes de la grille: ")
            label.pack()
            nb_col=Entry(self.fen, textvariable=self.__nb_col)
            nb_col.focus_set()
            nb_col.pack()
            button= Button(self.fen, text="Valider",command=self.dim_mines)
            button.pack()
            
        #si on mets 0 lignes    
        elif(self.__nb_lignes.get()==0): 
            tkinter.messagebox.showwarning(title="Erreur de saisie", message="Saisir un entier NON NUL !")
        #si la valeur n'est pas un nb    
        #elif(self.__nb_lignes.get().isdigit()==False):
        
            #print("Erreur sur le nb de lignes")
            #tkinter.messagebox.showwarning(title="Erreur de saisie", message="Saisir une valeur qui est un ENTIER <=26")
        #si on mets une valeur incorrecte
        else:
            
            print("Erreur sur le nb de lignes")
            tkinter.messagebox.showwarning(title="Erreur de saisie", message="Saisir un entier <=26")
            
            
    def dim_mines(self):
    
        #3/ Après validation, vérifie la valeur du nb de colonnes saisie
        #si la valeur est correcte on passe à la suite
        if(self.__nb_col.get()<=26 and self.__nb_col.get()!=0):
            #créer zone pour saisir le nb de mines
            self.__nb_mines=IntVar()
            label= Label (self.fen, text="Saisir le nombre de mines dans la grille: ")
            label.pack()
            nb_mines=Entry(self.fen, textvariable=self.__nb_mines)
            nb_mines.focus_set()
            nb_mines.pack()
            button= Button(self.fen, text="Valider",command=self.affiche_grille)
            button.pack()
            
        elif(self.__nb_col.get()==0): 
            tkinter.messagebox.showwarning(title="Erreur de saisie", message="Saisir un entier NON NUL !")
            
        
        
            print("Erreur sur le nb de colonnes")
            tkinter.messagebox.showwarning(title="Erreur de saisie", message="Saisir une valeur qui est un ENTIER <=26")
            
        else:
            
            print("Erreur sur le nb de colonnes")
            tkinter.messagebox.showwarning(title="Erreur de saisie", message="Saisir un entier <=26")
    
  
            
    def affiche_grille(self):
        
        #3/ Après validation, vérifie la valeur du nb de mines saisie
        #si la valeur est correcte (=toutes les cases ne sont pas des mines... ou qu'il y ait 0 mines) on passe à la suite
        if(self.__nb_mines.get()>0 and (self.__nb_lignes.get()*self.__nb_col.get()-(2*self.__nb_col.get()+2*self.__nb_lignes.get()-4)-self.__nb_mines.get()>0)):
            self.fen.destroy()
            #affiche la dim de la grille dans une minifen
            tkinter.messagebox.showinfo(title="Dimension grille", message=str(self.__nb_lignes.get())+"x" +str(self.__nb_col.get())+"+" +str(self.__nb_mines.get())+ " mines")
            
                     
            
     
            #génère une grille avec le nb de col et de ligne saisie
            
           
            
        elif(self.__nb_mines.get()==0):
            print("Erreur sur le nb de mines!")
            tkinter.messagebox.showwarning(title="Erreur de saisie", message="Saisir un entier NON NUL !")        
           
        else:
            print("Erreur sur le nb de mines!")
            tkinter.messagebox.showwarning(title="Erreur de saisie", message="Erreur sur le nb de mines")
        
        g1=Grille(self.__nb_lignes.get(), self.__nb_col.get())       
       
       
 
 
###3###
class Page_choix_niveau(Page):

    def __init__(self,nom):
    
        Page.__init__(self)
        self.titre="Choix du niveau" #pour une Page_nom le titre de la fen est modifié
        self.fen.title(self.titre) 
        self.nom= nom 
        self.nb_col=0
        self.nb_l=0
        
        
         
        l1= Label(self.fen, text = self.nom+ " sélectionne ton niveau :" , fg = lavande, font = ("Times New Roman", 20, "bold")) #zone de saisie de texte où on entre son nom
        l1.pack() 
        
        #création d'un frame dans lequel on affichera les bouton radios
        frame=Frame(self.fen)
        frame.place(x=50, y=80, width=20,height=20)
        frame.pack(fill=tkinter.Y, side=tkinter.RIGHT,expand=True)
        
        
        #affichage des 4 niveaux à l'aide de radio boutons
        self.v = StringVar(self.fen, "1")
 
        #dictionnaire pour créer les boutons radios
        values = {
            "Facile": "1",
            
            "Moyen": "2",
            
            "Difficile": "3",
            
           "Niveau personnalisé": "4"}
           
       #boucle for pour créer les différents radio boutons
        for (text, value) in values.items():
            Radiobutton(frame, text = text, variable = self.v,
            value = value).pack(side = TOP, ipady = 30)
            
        
        #création d'un frame dans lequel on affichera les bouton radios
        frame2=Frame(self.fen)
        frame2.place(x=50, y=150, width=20,height=20)
        frame2.pack(fill=tkinter.Y, side=tkinter.RIGHT,expand=True)
          
         #bouton pour accéder à la page suivante
        bs = Button(frame2, text ="Suivant",font = ("Times New Roman", 20,"italic","bold") ,height=2,width=5,fg=bleu,bg=lavande,command=self.page_suivante).pack(side=RIGHT)
        
        
        
        #bouton pour quitter
        bq = Button(frame2, text ="Quitter",font = ("Times New Roman", 20,"italic","bold") ,height=2,width=5,fg=lavande,bg=bleu,command=self.quitter_fen).pack(side=RIGHT)
        
 
        
         
    def page_suivante(self):
        self.fen.destroy()
        
        #en fonction du niv sélectionné, on a une dim de la grille != 
        if(self.v.get()=="1"):
            self.nb_col=5
            self.nb_l=5
            self.nb_m=7
            
            tkinter.messagebox.showinfo(title="Infos dim grille", message="Dimension de la grille: " +str(self.nb_l)+ "x" +str(self.nb_col)+" + "+str(self.nb_m)+ " mines") #affiche la dim de la grille
            
            
        elif(self.v.get()=="2"):
            self.nb_col=10
            self.nb_l=10
            self.nb_m=40
            tkinter.messagebox.showinfo(title="Infos dim grille", message="Dimension de la grille: " +str(self.nb_l)+ "x" +str(self.nb_col)+ " + "+str(self.nb_m)+ " mines")
            global pgi
            pgi=Page_grille_ini(self.nb_l,self.nb_col)
            
        elif(self.v.get()=="3"):
            self.nb_col=20
            self.nb_l=20
            self.nb_m=200
            tkinter.messagebox.showinfo(title="Infos dim grille", message="Dimension de la grille: " +str(self.nb_l)+ "x" +str(self.nb_col)+" + "+str(self.nb_m)+ " mines")
            
        else:
            p3=Page_niv_perso()
            
            
            
            
            
        
        
    def quitter_fen(self):
        self.fen.destroy()   
        
    #permet d'afficher la dim en fontion du niveau de difficulté choisi    
    #def choix_niv(self):
    
        
     
###2###       
class Page_bienvenue(Page): #la page d'accueil après avoir saisi son nom

    def __init__(self,nom): #prend en paramètre le nom saisi dans la page précédente
        
        Page.__init__(self)
        self.titre="Accueil" #pour une page_nom le titre de la fen est modifié
        self.fen.title(self.titre)  
        self.__nom= nom
        
        
        #affiche le nom du jeu
        l1= Label(self.fen, text = "Jeu du démineur", fg = lavande, font = ("Times New Roman", 35,"italic")) 
        l1.pack() 
        l2= Label(self.fen, text = "Bienvenue "+ self.__nom +" !" , fg = lavande, font = ("Times New Roman", 30, "bold")) #affiche Bienvenue suivi du non de l'util.
        l2.pack()          
        
       
        
        #bouton Commencer      
        bc = Button(self.fen, text ="Commencer",font = ("Times New Roman", 20,"italic","bold"), height=2, width=10,fg=bleu, bg=lavande,command=self.commencer).pack(side=TOP,padx=5,pady=30)
        
        #bouton Quitter
        bq = Button(self.fen, text ="Quitter",font = ("Times New Roman", 20,"italic","bold") ,height=2,width=10,fg=lavande,bg=bleu,command=self.quitter_fen).pack(side=TOP,padx=50,pady=60)
        
	
	
        tk= Label(self.fen, text = "interface  graphique implémentée par Kamély LUMIERE M1 GENIOMHE 20190541", fg = "#0023F5", font = ("Times New Roman", 10,"italic")) 
        tk.place(relx = 0.0,rely = 1.0,anchor ='sw')
        tk.pack()
        
        print("Nom utilisateur: ",self.__nom)
        
     
            
    def quitter_fen(self):
    
        self.fen.destroy()
       
    def commencer(self):
        self.fen.destroy()
        p3=Page_choix_niveau(self.__nom)  ##/!\permet de recup le nom saisi à la page_nom et l'utiliser dans la page suivante (choix_niveau)
       
        


###1###
class Page_nom(Page): #la page où on demande à l'uitlisateur de saisir son nom est une page "particulière" -> hérite de la classe Page

    #def __init__(self,lala):
    def __init__(self):
        
        
        
     
        #self.lala=lala #juste pour comprendre
        Page.__init__(self)
        self.titre="Nom joueur" #pour une page_nom le titre de la fen est modifié
        self.fen.title(self.titre)
        
        
        # Create text widget and specify size.
        l1= Label(self.fen, text = "Veuillez saisir votre nom :", fg = lavande, font = ("Times New Roman", 20, "bold")) #zone de saisie de texte où on entre son nom
        l1.pack() 
        self.__name=StringVar()
        
        nom=Entry(self.fen,textvariable=self.__name)
        nom.focus_set()
        nom.pack()
        #print("#####")
       
        #bouton pour accéder à la page suivante
        bs = Button(self.fen, text ="Suivant",font = ("Times New Roman", 20,"italic","bold") ,height=2,width=5,fg=bleu,bg=lavande,command=self.page_suivante).pack(side=RIGHT)
        
        
        
        #bouton pour quitter
        bq = Button(self.fen, text ="Quitter",font = ("Times New Roman", 20,"italic","bold") ,height=2,width=5,fg=lavande,bg=bleu,command=self.quitter_fen).pack(side=RIGHT)
        
    
    
    def recup_nom(self):
        return(self.__name.get())
    
    
    
        
    def page_suivante(self):
        self.fen.destroy() #on ferme la fenêtre puis on ouvre une nouvelle qui utilise le nom saisi par l'utilisateur
        p2=Page_bienvenue(Page_nom.recup_nom(self)) ##/!\permet de recup le nom saisi et l'utiliser dans la page suivante
        #p2=Page_bienvenue(self.__name.get()) #on peut faire ça aussi(équivalent à laligne d'avant)
        
        print(Page_nom.recup_nom(self))
            
            
        
        
    def quitter_fen(self):
    
        self.fen.destroy()
      
        
        

class Jeu():
 
    def __init__(self):
    
        p1=Page_nom()
    
     
## pour tester l'interface graphique "incomplète" du jeu
#j=Jeu()
#pn=Page_niv_perso()

##pour tester la fonctionnalité de ma classe Case
#c1=Case(0,1)
#c2=Case(0,2)
#c3=Case(1,0)
#c4=Case(7,1)
#c1.setVal("S")
#print(c1.getVal())
#print(c4.getLigne())
#print(c4.getCol())

##pour tester la fonctionnalité de la classe Grille--> ça fonctionne
g=Grille(10,10)
g.questions()
#print(g.self.__nb_l)
#g2=Grille_rep(g.nb_l,g.nb_col)



###ne pas toucher
tkinter.mainloop()


