import tkinter as tk
import time

NB_IMAGES = 1000

# Création de la fenêtre
root = tk.Tk()
root.title("Mesure du rendu seul")
root.geometry("800x600")

canvas = tk.Canvas(
    root,
    width=800,
    height=600,
    bg="black",
    highlightthickness=0
)
canvas.pack()

# Affichage initial
root.update()

# Petit échauffement
for _ in range(20):
    canvas.delete("all")
    root.update()

# Mesure du rendu seul
durees = []

for _ in range(NB_IMAGES):

    debut = time.perf_counter()

    # RENDU
    canvas.delete("all")

    # Force Tkinter à traiter immédiatement
    # les mises à jour de la fenêtre.
    root.update()

    fin = time.perf_counter()

    duree_ms = (fin - debut) * 1000
    durees.append(duree_ms)

# Résultats
moyenne = sum(durees) / len(durees)
plus_longue = max(durees)

# Estimation de deux rendus
rendu_deux_fois = moyenne * 2

# Budget restant sur 11 ms
reste = 11 - rendu_deux_fois

print("Nombre d'images :", NB_IMAGES)
print(f"Temps moyen du rendu seul : {moyenne:.6f} ms")
print(f"Plus long rendu : {plus_longue:.6f} ms")
print(f"Estimation du rendu effectué deux fois : {rendu_deux_fois:.6f} ms")
print(f"Temps restant sur 11 ms : {reste:.6f} ms")

root.destroy()