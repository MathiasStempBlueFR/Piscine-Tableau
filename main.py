import tkinter as tk 
from tkinter import ttk

fenetre =tk.Tk() #début de l'iterface

#Grid de gauche | zone d'ajout d'information
#Partie Label
L1 = tk.Label(fenetre, text="Ajout d'un nom", fg="black", bg="lightgrey", width="20")
L1.grid(column=0, row=0,)

L2 = tk.Label(fenetre, text="Ajout d'un type de nage", fg="black", bg="lightgrey", width="20")
L2.grid(column=0, row=1)

L3 = tk.Label(fenetre, text="Ajout d'une longueur", fg="black", bg="lightgrey", width="20")
L3.grid(column=0, row=2)

Linfo = tk.Label(fenetre, text="Tableau", fg="black", bg="lightgrey", width="30")
Linfo.grid(column=3, row=3)

#partie button
B = tk.Button(fenetre, text="Ajouter à la liste", fg="black", bg="lightgrey", width="20")
B.grid(column=1, row=3)

#Fonctionalité du bouton ajout


#partie entry

E1 = tk.Entry(fenetre, width=30)
E1.grid(column=1, row=0)

E2 = tk.Entry(fenetre, width=30)
E2.grid(column=1, row=1)

E3 = tk.Entry(fenetre, width=30)
E3.grid(column=1, row=2)


#data

Nom = ["Lea", "Pierre", "Yves", "Germain", "Dimitri", "Isidor"]
Nage = ["brasse", "crowl", "dos", "crowl", "brasse", "crowl"]
Longueur = [10, 12, 8, 10, 12, 10]

#Grid de droite | Le tableau

T = ttk.Treeview(fenetre, columns = ('Nom', 'Nage', 'Longueur'), show='headings')
T.heading('Nom', text="Nom")
T.heading('Nage', text="Nage")
T.heading('Longueur', text="Longueur")
T.grid(column=3, row=4)

for i in range(len(Nom)):
    data = (Nom[i], Nage[i], Longueur[i])
    T.insert(parent='', index = 0, values=data)

fenetre.geometry("1000x500") #fin de l'interface
fenetre.mainloop()

#Lien de Vidéo + Sites utilisés
#https://tkdocs.com/index.html
#https://www.youtube.com/watch?v=jRpHmF-iuMI