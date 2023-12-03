import tkinter as tk 
from tkinter import ttk

fenetre =tk.Tk() #début de l'iterface

#Grid de gauche | zone d'ajout d'information
B1 = tk.Button(fenetre, text="Ajout d'une longueur : ", fg="black", bg="lightgrey")
B1.grid(column=0, row=0)


B2 = tk.Button(fenetre, text="Ajout d'un nageur : ", fg="black", bg="lightgrey")
B2.grid(column=0, row=1)


B3 = tk.Button(fenetre, text="Ajout d'un type de nage : ", fg="black", bg="lightgrey")
B3.grid(column=0, row=2)



fenetre.geometry("700x500") #fin de l'interface
fenetre.mainloop()