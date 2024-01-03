
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
