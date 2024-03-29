import tkinter as tk
from tkinter import messagebox

# Fonction pour simuler la récupération de données
def simulate_data_retrieval():
    # Simulation de données locales
    data = ["Donnée 1", "Donnée 2", "Donnée 3"]
    # Afficher les données dans une boîte de dialogue
    messagebox.showinfo("Données récupérées", f"Données récupérées localement : {data}")

# Création de l'interface utilisateur
def create_ui():
    root = tk.Tk()
    root.title("Application sans API")

    label = tk.Label(root, text="Cliquez sur le bouton pour simuler la récupération des données")
    label.pack(pady=10)

    button = tk.Button(root, text="Récupérer les données", command=simulate_data_retrieval)
    button.pack(pady=5)

    root.mainloop()

# Point d'entrée de l'application
if __name__ == "__main__":
    create_ui()
