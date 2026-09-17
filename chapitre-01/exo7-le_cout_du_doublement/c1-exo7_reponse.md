# C1 — Exercice 7

## Mesure du rendu seul

Sur 1000 images, j'ai mesuré le temps pris par le rendu seul, sans la logique du programme.

- **Temps moyen du rendu seul : 0,0020 ms**
- **Plus long rendu : 0,0565 ms**

## Estimation d'un rendu effectué deux fois

Pour estimer le coût d'un rendu effectué deux fois, je double le temps moyen mesuré :

0,0020 × 2 = 0,0039 ms

Soit une estimation d'environ **0,0039 ms** pour deux rendus.

## Temps restant sur une enveloppe de 11 ms

11 - 0,0039 = 10,9961 ms

Il resterait donc environ **10,9961 ms** pour la logique du programme et les autres traitements.

## Conclusion

Dans cette mesure, le rendu seul ne constitue pas le principal coût temporel. Même en effectuant le rendu deux fois, son coût estimé reste très faible devant l'enveloppe de 11 ms.

Il faudrait donc surtout réduire les traitements qui prennent du temps ailleurs dans le programme : logique, calculs, physique, gestion des données ou autres opérations nécessaires à chaque image.

Le principe important pour un casque est qu'effectuer deux rendus, comme pour deux points de vue stéréoscopiques, ne signifie pas automatiquement dépasser la contrainte temporelle. Il faut surtout surveiller les parties du programme qui consomment réellement le budget restant.
