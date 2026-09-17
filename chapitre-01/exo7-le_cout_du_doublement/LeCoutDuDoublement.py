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

# Permet d'afficher correctement la fenêtre avant la mesure
root.update()

durees_rendu = []


# MESURE DU RENDU SEUL

for _ in range(NB_IMAGES):

    debut = time.perf_counter()
    
    # RENDU
    canvas.delete("all")
    root.update_idletasks()
    

    fin = time.perf_counter()

    duree_ms = (fin - debut) * 1000
    durees_rendu.append(duree_ms)

# RESULTATS

moyenne = sum(durees_rendu) / len(durees_rendu)
plus_longue = max(durees_rendu)

# Estimation si on faisait le même rendu deux fois
rendu_x2 = moyenne * 2

# Temps restant sur une enveloppe de 11 ms
reste = 11 - rendu_x2

print("Nombre d'images :", NB_IMAGES)
print(f"Temps moyen du rendu seul : {moyenne:.4f} ms")
print(f"Plus long rendu : {plus_longue:.4f} ms")
print(f"Estimation du rendu effectué deux fois : {rendu_x2:.4f} ms")
print(f"Temps restant sur 11 ms : {reste:.4f} ms")

root.destroy()