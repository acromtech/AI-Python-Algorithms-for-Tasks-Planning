# ai_algorithms_module

## Contexte

Notre robot R2D2, évolue dans un monde 2D représenté par un graphe non orienté. Les arêtes du graphe représentent les routes que R2D2 peut emprunter, et les sommets représentent les lieux où R2D2 doit effectuer des tâches. Chaque arête est pondérée pour représenter la longueur du chemin, et chaque sommet est pondéré par sa position dans le plan 2D.

La mission de R2D2 est de déposer un cube de couleur à chaque lieu de manière à ce que des cubes de couleurs différentes se trouvent dans deux lieux voisins (liés par une arête). Trois principales tâches sont identifiées.

## Planning

Le projet est découpé en 5 étapes réparties sur 12 séances de TP.

1. **Étape 1 (TP 1 et 2):** Résolution de la tâche 1 - Utilisation de la logique propositionnelle pour déterminer si trois couleurs sont suffisantes. Utilisation du solver SAT.

2. **Étape 2 (TP 3 à 6):** Résolution de la tâche 2 - Calcul des chemins les plus courts entre lieux. Trois cas sont abordés, chacun utilisant des algorithmes différents.

    - **Cas 1 :** Calcul du plus court chemin entre deux lieux en utilisant les distances et les coordonnées cartésiennes.
    - **Cas 2 :** Recherche du chemin le plus court passant une fois par chaque lieu et revenant au point de départ.
    - **Cas 3 :** Intégration de la capacité de vol de R2D2, permettant des déplacements en ligne droite entre les lieux.

3. **Étape 3 (TP 7 et 8):** Suite de la tâche 2 - Optimisation des méthodes pour calculer des chemins moins optimaux mais plus rapidement.

4. **Étape 4 (TP 9 et 10):** Résolution de la tâche 3 - Utilisation d'un graphe de contraintes pour déterminer le nombre minimal de couleurs nécessaires.

5. **Étape 5 (TP 11 et 12):** Suite et fin de la tâche 2 - Résolution du cas 3 de la tâche 2 en exprimant le problème à l'aide de formules mathématiques (utilisation de ZIMPL et SCIP).

## Lancement du programme
1. **Assurez-vous d'être dans le répertoire du dépôt après le téléchargement.**
```
cd [chemin/vers/le/dépôt]
```
2. **Exécutez le programme**
```
make all
```
3. **Les résultats sont affichés dans le fichier `log` à côté du Makefile**

## Dépendances

Lors du lancement du programme (`make all`), il vérifiera que les dépendances sont installées, sinon **il les ajoutera automatiquement** :
* python-sat
* python-constraint

