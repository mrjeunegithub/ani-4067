import tkinter as tk
import time

# Nombre d'images à mesurer
NB_IMAGES = 1000

# Liste qui contiendra la durée de chaque image, en millisecondes
durees = []

# Création de la fenêtre
root = tk.Tk()
root.title("Mesure du temps de rendu")
root.geometry("800x600")

# Zone de dessin
canvas = tk.Canvas(root, width=800, height=600,
                   bg="black", highlightthickness=0)
canvas.pack()


def mesurer_image():
    # On commence le chronomètre
    debut = time.perf_counter()

    # Travail graphique de l'image
    canvas.delete("all")

    # On force Tkinter à effectuer les opérations graphiques en attente
    root.update_idletasks()

    # Fin du chronomètre
    fin = time.perf_counter()

    # Conversion en millisecondes
    duree_ms = (fin - debut) * 1000

    # On mémorise la durée
    durees.append(duree_ms)

    # Tant qu'on n'a pas atteint 1000 images,
    # on mesure l'image suivante
    if len(durees) < NB_IMAGES:
        root.after(1, mesurer_image)
    else:
        # Résultats
        pire_image = max(durees)
        nb_depassements = sum(
            duree > 11 for duree in durees
        )

        print("Nombre d'images :", len(durees))
        print(f"Plus longue image : {pire_image:.2f} ms")
        print(f"Images dépassant 11 ms : {nb_depassements}")

        root.destroy()


# Lancement de la mesure
mesurer_image()

# Boucle graphique
root.mainloop()