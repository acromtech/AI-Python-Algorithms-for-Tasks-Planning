from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat

class EtatCas1(Etat) : # Classe pour definir un etat pour le cas 1 de la tache 2 (hérite de Etat)
    # ATTRIBUTS
    tg : GrapheDeLieux # le graphe representant le monde

    # CONSTRUCTEUR
    def __init__(self, tg : GrapheDeLieux, etat_debut=None, etat_final=None) :
        self.tg            = tg
        self.etat_courant  = etat_debut
        self.etat_final    = etat_final

    # METHODES issues de Etat
    def estSolution(self) : # Methode detectant si l'etat est une solution :return true si l'etat courant est une solution, false sinon
        return self.etat_courant == self.etat_final

    def successeurs(self) : # Methode permettant de recuperer la liste des etats successeurs de l'etat courant :return liste des etats successeurs de l'etat courant
        tab = []
        for adjacent in self.tg.getAdjacents(self.etat_courant):
          tab.append(EtatCas1(self.tg,adjacent, self.etat_final))
        return tab

    def h(self) :   # Methode permettant de recuperer l'heuristique de l'etat courant :return heuristique de l'etat courant
        return GrapheDeLieux.dist(self.etat_courant, self.etat_final , self.tg)

    def k(self, e) : # Methode permettant de recuperer le cout du passage de l'etat courant à l'etat e
        return self.tg.getCoutArete(self.etat_courant, e)

    def displayPath(self, pere) :
        chemin = [self.etat_final]
        courant = self.etat_final
        while courant != None:
            courant = pere[courant]
            chemin.append(courant)
        print("Sur",self.tg.getNbSommets(),"villes de",chemin[-2]," à ",chemin[0]," : ["," ".join(str(etat) for etat in chemin[:-1]),"]")

    # METHODES pour pouvoir utiliser cet objet dans des listes et des map
    def __hash__(self) : # Methode permettant de recuperer le code de hachage de l'etat courant pour une utilisation dans des tables de hachage -> return code de hachage
        return hash(self.etat_courant)

    def __eq__(self, o) :# Methode de comparaison de l'etat courant avec l'objet o -> return true si l'etat courant et o sont egaux, false sinon
        return self.etat_courant == o

    # METHODES pour affichage futur (heritee d'Object)
    def __str__(self) : # Methode mettant l'etat courant sous la forme d'une chaine de caracteres en prevision d'un futur affichage
        return str(self.etat_courant)



