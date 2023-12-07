#////////////////////////////////////////////////////////////////
#
#
# Pour votre devoir 
#
#
#////////////////////////////////////////////////////////////////

#
#   Gestionnaire de piscine
#

def ajoutNageur(liste:list):
    """Ajoute une personne qui réalise une nage pendant certain nombre de longueur"""
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = input("combien de longueur ? ")
    liste.append((a,b,c))


def listeNageurs(liste:list):
    """Liste toutes les performances de tous les nageurs"""
    for elt in liste:
        #print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}")
        print("Prénom ",elt[0], " nage ",elt[1], " longueur ", elt[2])


def listeIndividu(liste:list):
    """Liste toutes les performances d'un individu en particulier"""
    nom = input("Qui ? ")
    print("Prénom du nageur: ", nom)
    for elt in liste:
        if elt[0]==nom:
         print(f"nage {elt[1]}, longueur {elt[2]}")


def listeNage(liste:list):
    """Liste tous les nageurs en fonction d'une nage particulière"""
    nage = input("Quelle nage ? ")
    print("Nage considée ", nage)
    for elt in liste:
        if elt[1]==nage:
            print(f"Prénom {elt[0]}, longueur {elt[2]}")


def simplifyCase(ch: str):
    """Traitement de la chaine pour simplification des IO"""
    return ch.lower()


def checkIfExit()-> bool:
    """Demande confirmation pour quitter le programme"""
    ch = input("En êtes vous sûr ? oui ou non ")
    if simplifyCase(ch) == "oui":
        return False
    else :
        return True

def listeSave(l):
    """Sauvegarde les informations dans un fichier"""
    myfile = open("piscine_database.txt","w")
    for elt in l:
        s = elt[0]+','+ elt[1]+','+str(elt[2])+'\n'
        myfile.write(s)
    myfile.close()

def listeLoad(l):
    """charge les informations stockées dans un fichier"""
    myfile = open("piscine_database.txt","r")
    for line in myfile:
        line = line [:-1] # suppression du '\n' en fin de chaine
        aux = line.split(',') # je splite l en morceaux
        # je convertis cela en un tuple
        elt = (aux[0], aux[1], int(aux[2]))
        l.append(elt)
    myfile.close()


liste = []
# des exemples pour peupler la liste
liste.append(('Léa','brasse',10))
liste.append(('Léa','crawl',12))
liste.append(('Léa','brasse',8))
liste.append(('Pierre','brasse',10))
liste.append(('Pierre','crawl',12))
liste.append(('Yves','brasse',10))

# variable controlant le while
isAlive = True

# boucle principale
while isAlive:
    commande = input("Que faut-il faire ? ")
    commande = simplifyCase(commande)

    if commande == 'ajout':
        ajoutNageur(liste)
        continue

    if commande == 'liste':
        listeNageurs(liste)
        continue

    if commande == 'individu':
        listeIndividu(liste)
        continue

    if commande == 'nageur':
        listeNage(liste)
        continue

    if commande == 'save':
        listeSave(liste)
        continue

    if commande == 'load':
        listeLoad(liste)
        continue

    if commande == 'exit':
        isAlive = checkIfExit()
        continue

    print(f"commande {commande} inconnue")

print("Fin du programme")