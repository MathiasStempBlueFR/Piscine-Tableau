import tkinter as tk 
from tkinter import ttk

fenetre =tk.Tk() #début de l'iterface

#Grid de gauche | zone d'ajout d'information
#partie button
B1 = tk.Button(fenetre, text="Ajout d'une longueur", fg="black", bg="lightgrey", width="20")
B1.grid(column=0, row=0,)


B2 = tk.Button(fenetre, text="Ajout d'un nom", fg="black", bg="lightgrey", width="20")
B2.grid(column=0, row=1)


B3 = tk.Button(fenetre, text="Ajout d'un type de nage", fg="black", bg="lightgrey", width="20")
B3.grid(column=0, row=2)

Badd = tk.Button(fenetre, text="Ajouter à la liste", fg="black", bg="lightgrey", width="20")
Badd.grid(column=1, row=3)

#partie entry

E1 = tk.Entry(fenetre, width=30)
E1.grid(column=1, row=0)

E2 = tk.Entry(fenetre, width=30)
E2.grid(column=1, row=1)

E3 = tk.Entry(fenetre, width=30)
E3.grid(column=1, row=2)

fenetre.geometry("700x500") #fin de l'interface
fenetre.mainloop()