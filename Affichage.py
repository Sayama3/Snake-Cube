from tkinter import *

def creationCube(): #interface pour l'utilisateur et lui permettre de rentré la position de son cube.

    #définition du plan dans la liste
    Position = 30
    haut1 = [-1]*29
    milieu = [-1]+[0]*27+[-1]
    milieu = milieu*27
    serpent = list()

    cube = haut1 + milieu + haut1

    class Interface(Frame):
        
        """Notre fenêtre principale.
        Tous les widgets sont stockés comme attributs de cette fenêtre."""
        
        def __init__(self, fenetre, **kwargs):
            Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
            self.pack(fill=BOTH)
            self.Position = 30#position initial
            self.last = int() #entier qui correspond à la dernière action
            self.last2 = list() #liste contenant toute les actions
            
            self.nombre = int(0) #c'est le numérotième cube fait
            self.Ordre = list() # c'est pour connaitre l'ordre des action effectuer
            
            # Création des widgets
            self.Space = Label(self, text=" ")
            self.space = Label(self, text=" ")
            self.Espace = Label(self, text=" ")
            self.espace = Label(self, text =" ")
            
            self.alert = Label(self, text = "")
            self.serpent = Label(self, text = "Il n'y a pas de cube.")
            self.ordre = Label(self, text = "")
            
            # Maintenant c'est le texte et tout les boutons
            
            self.serpent.pack(fill=X)
            self.ordre.pack(fill=X)
            self.alert.pack(fill=X)
            
            self.start = Button(self, text = "Pour quand ça commmence", command = self.Start)
            self.start.pack(fill=X)

            self.space.pack(fill=X)
            
            self.xplus = Button(self, text="Ajouter en X+", command = self.Xplus)
            self.xplus.pack(fill=X)

            self.xmoins = Button(self, text="Ajouter en X-", command = self.Xmoins)
            self.xmoins.pack(fill=X)

            self.Space.pack(fill=X)
            
            self.yplus = Button(self, text="Ajouter en Y+", command = self.Yplus)
            self.yplus.pack(fill=X)

            self.ymoins = Button(self, text="Ajouter en Y-", command = self.Ymoins)
            self.ymoins.pack(fill=X)
            

            self.Espace.pack(fill=X)

            self.annuler = Button(self, text="Annuler la dernière action", command = self.Annuler)
            self.annuler.pack(fill=X)

            self.espace.pack(fill=X)

            self.quitter = Button(self, text = "Terminer", command = self.Quitter)
            self.quitter.pack(fill=X)

        # Ici c'est les fonction pour créer le serpent
        
        def Start(self): #fonction qui permet d'initialiser la première variable
            if self.nombre == 0:
                cube[self.Position] = self.nombre
                self.nombre +=1
                self.serpent["text"] = "C'est le cube {}".format(self.nombre)
                self.alert["text"] = ""
                self.Ordre.append("Start")
                self.ordre["text"] = "{}".format(self.Ordre)
                self.start["text"] = ""
                serpent.append("Start")
            else:
                self.alert["text"] = "On a déjà commencé"

                
        def Xplus(self): #ajouter un élément en +X (orienté dans le plan)
            self.last = 1
            self.Position = self.Position + self.last
            self.last2.append(self.last)
            
            
            if cube[self.Position]== 0: #Le test ici c'est pour vérifier qu'on peut bien mettre le cube et qu'il n'y a pas d'erreur
                cube[self.Position] = self.nombre+1
                self.nombre +=1
                self.serpent["text"] = "C'est le cube {}".format(self.nombre)
                self.alert["text"] = ""
                
                self.Ordre.append("+X")
                serpent.append("+X")
                self.ordre["text"] = "{}".format(self.Ordre)
                
            elif cube[self.Position] == -1:
                self.alert["text"] = "Euh... il y a une erreur, le cube ne peut pas être là..."
                self.Position = self.Position - self.last
                del self.last2[-1]
            else:
                self.alert["text"] = "Il y a déjà un cube ici..."
                self.Position = self.Position - self.last
                del self.last2[-1]

                
            
                
        def Xmoins(self): #ajouter un élément en -X (orienté dans le plan)
            self.last = -1
            self.Position = self.Position + self.last
            self.last2.append(self.last) 
            
            if cube[self.Position]== 0: #Le test ici c'est pour vérifier qu'on peut bien mettre le cube et qu'il n'y a pas d'erreur
                cube[self.Position] = self.nombre+1
                self.nombre +=1
                self.serpent["text"] = "C'est le cube {}".format(self.nombre)
                self.alert["text"] = ""
                
                self.Ordre.append("-X")
                self.ordre["text"] = "{}".format(self.Ordre)
                serpent.append("-X")
                
            elif cube[self.Position] == -1:
                self.alert["text"] = "Euh... il y a une erreur, le cube ne peut pas être là..."
                self.Position = self.Position - self.last
                del self.last2[-1]
            else:
                self.alert["text"] = "Il y a déjà un cube ici..."
                self.Position = self.Position - self.last
                del self.last2[-1]

                
            

        def Ymoins(self): #ajouter un élément en -Y (orienté dans le plan)
            self.last = -29
            self.Position = self.Position + self.last
            self.last2.append(self.last)
            
            if cube[self.Position]== 0: #Le test ici c'est pour vérifier qu'on peut bien mettre le cube et qu'il n'y a pas d'erreur
                cube[self.Position] = self.nombre+1
                self.nombre +=1
                self.serpent["text"] = "C'est le cube {}".format(self.nombre)
                self.alert["text"] = ""
                
                self.Ordre.append("-Y")
                self.ordre["text"] = "{}".format(self.Ordre)
                serpent.append("-Y")
                
            elif cube[self.Position] == -1:
                self.alert["text"] = "Euh... il y a une erreur, le cube ne peut pas être là..."
                self.Position = self.Position - self.last
                del self.last2[-1]
            else:
                self.alert["text"] = "Il y a déjà un cube ici..."
                self.Position = self.Position - self.last
                del self.last2[-1]

                
            

        def Yplus(self): #ajouter un élément en +Y (orienté dans le plan)
            self.last = 29
            self.Position = self.Position + self.last
            self.last2.append(self.last)
            
            if cube[self.Position]== 0: #Le test ici c'est pour vérifier qu'on peut bien mettre le cube et qu'il n'y a pas d'erreur
                cube[self.Position] = self.nombre+1
                self.nombre +=1
                self.serpent["text"] = "C'est le cube {}".format(self.nombre)
                self.alert["text"] = ""
                
                self.Ordre.append("+Y")
                self.ordre["text"] = "{}".format(self.Ordre)
                serpent.append("+Y")
            elif cube[self.Position] == -1:
                self.alert["text"] = "Euh... il y a une erreur, le cube ne peut pas être là..."
                self.Position = self.Position - self.last
                del self.last2[-1]
            else:
                self.alert["text"] = "Il y a déjà un cube ici..."
                self.Position = self.Position - self.last
                del self.last2[-1]

                
            

        def Annuler(self): #fonction servant à annuler une action
            if self.nombre > 1:
                cube[self.Position] = 0
                self.Position = self.Position - self.last2[-1]
                del self.last2[-1]
                self.nombre -=1
                self.serpent["text"] = "C'est le cube {}".format(self.nombre)
                del self.Ordre[-1]
                del serpent[-1]
                self.ordre["text"] = "{}".format(self.Ordre)
            
            else:
                self.alert["text"] = "Tu ne peux pas annuler, il n'y a rien à annuler"



        def Quitter(self): #fonction servant à Quitter
            if len(self.Ordre) == 27:
                fenetre.quit()
            else:
                self.alert["text"] = "Tu ne peux pas quitter tant qu'il n'y a pas 27 cubes"


    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()
    return serpent



def analyse(cube): #fonctions tranformant la liste de "+X", "-Y"... en une liste de droite jusqu'au prochain angle droit
    
    #première étape
    
    if cube[1] == '+X':
        cube[0] = '+X'
    elif cube[1] == '-X':
        cube[0] = '-X'
    elif cube[1] == '+Y':
        cube[0] = '+Y'
    elif cube[1] == '-Y':
        cube[0] = '-Y'

        
    #deuxième étapes
        
    snake = list() #c'est le serpent final
    accumulateur = int() #c'est un accumulateur qui va servir a compter le nombre de cube.
    for i in range(len(cube)):
        if i == 0:
            if cube[i] == '+X' or cube[i] == '+Y':
                accumulateur = 1
            else:
                accumulateur = -1
        else:
            if cube[i] == cube [i-1]:
                if cube[i] == '+X' or cube[i] == '+Y':
                    accumulateur += 1
                else:
                    accumulateur -= 1
            else:
                snake.append(accumulateur)
                if cube[i] == '+X' or cube[i] == '+Y':
                    accumulateur = 1
                else:
                    accumulateur = -1

    snake.append(accumulateur)
    return snake


def visualisationCube(cube):
    """ Affichage du cube """
    print("face n°1 :")
    print(cube[31],cube[32],cube[33])
    print(cube[36],cube[37],cube[38])
    print(cube[41],cube[42],cube[43])
    
    print("")
    print("face n°2 :")
    print(cube[56],cube[57],cube[58])
    print(cube[61],cube[62],cube[63])
    print(cube[66],cube[67],cube[68])

    print("")
    print("face n°3 :")
    print(cube[81],cube[82],cube[83])
    print(cube[86],cube[87],cube[88])
    print(cube[91],cube[92],cube[93])

    print("")

    print("-----")

    i = input('appuyé sur "entrée" pour continuer\n')

def constructionSnake(): #raccourcis pour créer le cube
    cube = creationCube()
    snake = analyse(cube)
    return snake
    
    
if __name__ == "__main__": # vérification pour tester les différents sous-progromme créer
    j = 0
    snake = list()

    phase0 = ['Start', '+X', '+X', '+X', '+X', '+Y', '+Y', '+Y', '+Y', '-X', '-X', '-X', '+Y', '+Y', '+Y', '+X', '+X', '+X', '+X', '+Y', '+X', '-Y', '-Y', '-Y', '-Y', '+X', '+X']
    phase1 = [1,1,1,1,2,2,2,2,-1,-1,-1,-1,-2,-2,-2,-2]
    a = analyse(phase0)
    print(a)
