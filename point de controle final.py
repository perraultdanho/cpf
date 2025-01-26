import tkinter as tk

# Fonction de conversion Fahrenheit -> Celsius
def fahrenheit_to_celsius():
    try:
        # Récupérer la température en Fahrenheit
        fahrenheit = float(ent_temperature.get())
        # Conversion en Celsius
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        # Afficher le résultat arrondi à 2 décimales
        lbl_result.config(text=f"{round(celsius, 2)}\N{DEGREE CELSIUS}")
    except ValueError:
        # Si la valeur entrée n'est pas un nombre valide
        lbl_result.config(text="Entrée invalide")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Convertisseur de Température")
window.resizable(width=False, height=False)

# Création du cadre pour l'entrée de température
frm_entry = tk.Frame(master=window)

# Widget d'entrée pour la température en Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Widget label pour afficher le symbole de degré Fahrenheit
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Disposition des widgets dans le cadre
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Création du bouton de conversion
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)

# Widget label pour afficher le résultat en Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Disposition des widgets dans la fenêtre principale
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Lancer la boucle principale de l'application
window.mainloop()
