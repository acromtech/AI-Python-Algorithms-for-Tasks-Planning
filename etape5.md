## Etape 5

**Etape 5 = TP 11 et 12** Réalisation de la tâche 2 (suite et fin).

Comme R2D2 aime aussi beaucoup les maths et qu’il veut épater ses concepteurs, il reprend le cas 3 de la tâche 2, et cherche à le résoudre en l’exprimant à l’aide de formules mathématiques. Vous devrez proposer un encodage approprié utilisant le langage ZIMPL et résoudre le problème en utilisant le solver SCIP.


**Installation de l'environnement de travail**


*   récupération de l'outil SCIP sur votre machine (voir le README dans la documentation sur ZIMPL et sur SCIP qui se trouve dans le fichier *Doc.zip* que vous pouvez télécharger depuis la liste des fichiers et installer en le décompressant sur votre machine.)
*   compression du répertoire SCIP sur votre machine (celui qui contient les 3 sous-répertoire "bin", "lib" et "include") pour créer le fichier *SCIP.zip*
*   puis avec le bloc de code suivant : upload du fichier *SCIP.zip* sur GoogleCoLab, décompression et test avec le code ZIMPL donné

```
!rm -r SCIP
!unzip SCIP.zip
!SCIP/bin/scip -f projet/etape5/test.zpl
```

**Exemple de code ZIMPL utilisé pour le test précédent :** il correspond à l'exemple vu en cours (résultat attendu : x1 = 4, x2 = 0 pour une valeur de 68)

```py
var x1 integer >= 0 ;
var x2 integer >= 0 ;
maximize res : (17 * x1) + (12 * x2) ;
subto c1 : (10 * x1) + (7 * x2) <= 40 ;
subto c2 : x1 + x2 <= 5 ;
```


**Le travail à faire**

Ecrire un programme ZIMPL répondant à la question posée. Ce programme sera à placer et à tester sur le modèle du bloc de code suivant.

Si vous définissez plusieurs programmes ZIMPL, vous devrez faire un bloc de code par programme. Attention à bien choisir le nom des fichiers de sauvegarde pour ne pas en écraser.


```py
contenuFichierZIMPL = """
    var x1 integer >= 0 ;
    var x2 integer >= 0 ;
    maximize res : (17 * x1) + (12 * x2) ;
    subto c1 : (10 * x1) + (7 * x2) <= 40 ;
    subto c2 : x1 + x2 <= 5 ;
    """

with open('projet/etape5/fichier1.zpl', 'w') as f:
  f.write(contenuFichierZIMPL)

!SCIP/bin/scip -f projet/etape5/fichier1.zpl
```
**Output**
```
SCIP/bin/scip: error while loading shared libraries: libtbb.so.2: cannot open shared object file: No such file or directory
```


**Autre cas**
```py
# Définir le contenu du fichier ZIMPL pour 6 villes
contenuFichierZIMPL6 = """
    # Déclaration des variables
    var x01 binary;
    var x02 binary;
    var x03 binary;
    var x04 binary;
    var x05 binary;
    var x06 binary;

    # Fonction objectif à maximiser
    maximize res : (poids01 * x01) + (poids02 * x02) + (poids03 * x03) + (poids04 * x04) + (poids05 * x05) + (poids06 * x06);

    # Contraintes
    subto c1 : x01 + x02 + x03 + x04 + x05 + x06 = 6;
    subto c2 : (sommet1 * x01) + (sommet2 * x02) + (sommet3 * x03) + (sommet4 * x04) + (sommet5 * x05) + (sommet6 * x06) = 6;
    # ... Ajoutez d'autres contraintes au besoin ...
"""

# Enregistrez le fichier ZIMPL sur le disque
with open('projet/etape5/fichier6.zpl', 'w') as f:
  f.write(contenuFichierZIMPL6)

!SCIP/bin/scip -f projet/etape5/fichier6.zpl
```
**Output**
```
SCIP/bin/scip: error while loading shared libraries: libtbb.so.2: cannot open shared object file: No such file or directory
```


# SOUMA

from google.colab import files
contenuFichierZIMPL = """
  set V     :=  {1..num_villes};
  set E     := { <i , j > in V * V with i < j };
  set P[]  := powerset (V ) ;
  set K     := indexset (P ) ;

  param px[V]:= read "../../Data/pb-etape5/tsp6.txt" as "1n" skip 4;
  param py[V]:= read "../../Data/pb-etape5/tsp6.txt" as "2n" skip 4;

  defnumb dist(a, b) := sqrt((px[a] - px[b])^2 + (py[a] - py[b])^2);

  var x [E] binary ;
  minimize cost : sum <i,j> in E : dist (i,j) * x [i,j] ;
  subto two_connected : forall <v> in V do
      (sum <v, j> in E : x [v, j] ) + (sum<i, v> in E : x [i, v] ) == 2;
  subto no_subtour :
    forall <k> in K with card(P[k]) > 2 and card(P[k]) < card(V) - 2 do
        sum <i, j> in E with <i> in P[k] and <j> in P[k] : x[i, j] <= card(P[k]) - 1;


"""

contenuFichierZIMPL = contenuFichierZIMPL.replace("num_villes", str(6))

# Enregistrez le fichier ZIMPL sur le disque
with open('projet/etape5/fichier6.zpl', 'w') as f:
  f.write(contenuFichierZIMPL)

!SCIP/bin/scip -f projet/etape5/fichier6.zpl
