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
            self.Position = 30
            self.last = int()
            self.last2 = list()
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
        
        def Start(self):
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

                
        def Xplus(self):
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

                
            
                
        def Xmoins(self):
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

                
            

        def Ymoins(self):
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

                
            

        def Yplus(self):
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

                
            

        def Annuler(self):
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



        def Quitter(self):
            if len(self.Ordre) == 27:
                fenetre.quit()
            else:
                self.alert["text"] = "Tu ne peux pas quitter tant qu'il n'y a pas 27 cubes"


    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()
    return serpent




def analyse(cube): #première étapes pour transformer le cube créer en une liste de chiffres
    phase1 = list()
    snake = list()
    base = 1

    
    for i in range(len(cube)):
        if cube[i] == 'Start': 
            phase1 = [base]
        if i == 1:
            if cube[i] == '+X' or cube[i] == '-X':
                X = base
                Y = base + 1
            else:
                Y = base
                X = base + 1

        if cube[i] == '+X':
            phase1.append(X)
        elif cube[i] == '-X':
            phase1.append(-X)
        elif cube[i] == '+Y':
            phase1.append(Y)
        elif cube[i] == '-Y':
            phase1.append(-Y)

        if len(phase1) == 27:
            snake = analyse2(phase1)
    return snake

def analyse2(phase1): #deuxième étapes pour transformer la liste de chiffre en une liste de droite jusqu'au prochain angle droit
    test = bool()
    verif1 = int()
    verif2 = int()
    verif3 = int()
    phase2 = list()
    
    for i in range(len(phase1)):
        if i == 0:
            verif1 = phase1[i]
            verif3 = verif1
            
            if verif1 == 2 or verif1 == -2:
                verif1 = int(verif1/2)
            
        
        if phase1[i] == verif3:
            verif2 += verif1
        else:
            phase2.append(verif2)
            verif1 = phase1[i]
            verif3 = verif1
            
            if verif1 == 2 or verif1 == -2:
                verif1 = int(verif1/2)
                
            verif2 = verif1
    phase2.append(verif2)
    return phase2


def visualisationCube(cube): #afficher le cube
    """ Affichage du cube """
    print(cube[31],cube[32],cube[33])
    print(cube[36],cube[37],cube[38])
    print(cube[41],cube[42],cube[43])

    print("")

    print(cube[56],cube[57],cube[58])
    print(cube[61],cube[62],cube[63])
    print(cube[66],cube[67],cube[68])

    print("")

    print(cube[81],cube[82],cube[83])
    print(cube[86],cube[87],cube[88])
    print(cube[91],cube[92],cube[93])

    print("")

    print("-----")


if __name__ == "__main__": # vérification pour tester les différents sous-progromme créer
    phase0 = list()
    snake = list()

    phase0 = ['Start', '+X', '+X', '+X', '+X', '+Y', '+Y', '+Y', '+Y', '-X', '-X', '-X', '+Y', '+Y', '+Y', '+X', '+X', '+X', '+X', '+Y', '+X', '-Y', '-Y', '-Y', '-Y', '+X', '+X']
    phase1 = [1,1,1,1,2,2,2,2,-1,-1,-1,-1,-2,-2,-2,-2]
