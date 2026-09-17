# C1 — Exercice 6

## Mesure sur 1000 images

J'ai mesuré le temps de traitement de 1000 images avec mon programme.

- **Nombre d'images mesurées :** 1000
- **Durée de la plus longue image :** 34,72 ms
- **Nombre d'images dépassant 11 ms :** 1

## Conclusion

Le programme ne respecterait pas parfaitement la contrainte temporelle demandée pour un casque.

En effet, la quasi-totalité des images reste sous 11 ms, mais une image atteint **34,72 ms**, soit largement au-dessus du seuil. Cette image représente **1 image sur 1000**, donc l'anomalie est rare, mais elle montre qu'il existe un pic de temps de calcul.

Le programme est donc **presque conforme**, mais il ne garantit pas que toutes les images seront produites assez rapidement. Pour une utilisation en casque, ces images ponctuellement trop longues peuvent provoquer une irrégularité d'affichage et dégrader le confort.
