import tkinter as tk
# Création de la fenêtre principale
root = tk.Tk()
root.title("conduite")
root.geometry("400x300") # Taille de la fenêtre
# Lancement de la boucle principale
root = tk.Tk()
root.title("test routier")
# Création d'un label
label = tk.Label(root, text="test routier",
font=("Arial", 20))
label.pack(pady=25)

def bouton_clique () :
   print("Bouton cliqué !")
root = tk.Tk()
root.title("Exemple de Bouton")# Création d'un bouton
button = tk.Button(root, text="Clique-moi",
command=bouton_clique)
button.pack(pady=20)
root.mainloop()
