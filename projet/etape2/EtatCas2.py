from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat
from projet.solvers.SolverAStar import SolverAStar

class EtatCas2(Etat):
    tg: GrapheDeLieux  # Le graphe représentant le monde

    # CONSTRUCTEUR
    def __init__(self, tg: GrapheDeLieux, etat_visit=None, etat_courant=0, etat_debut=0):
        self.tg = tg
        self.etat_courant = etat_courant
        self.etat_debut = etat_debut

        # Ajout de l'état courant dans l'ensemble des états qui ont déjà été visités
        if etat_visit is None:
            self.etat_visit = []
        else:
            self.etat_visit = etat_visit
        self.etat_visit.append(etat_courant)

    # METHODES issues de Etat
    def estSolution(self):
        # Vérifie si tous les états ont été visités et si le point de départ est également le point d'arrivée
        return len(self.etat_visit) == self.tg.getNbSommets() + 1 and self.etat_debut == self.etat_courant

    def successeurs(self):
        tableau = []

        # Si tous les états ont été visités et que le point de départ est adjacent au dernier état visité,
        # alors on crée un état supplémentaire pour revenir au point de départ
        if len(self.etat_visit) == self.tg.getNbSommets() and (self.etat_debut in self.tg.getAdjacents(self.etat_courant)):
            return [EtatCas2(self.tg, self.etat_visit.copy(), self.etat_debut, self.etat_debut)]

        # Ajoute tous les états adjacents non visités dans le tableau
        for adjacent in self.tg.getAdjacents(self.etat_courant):
            if adjacent not in self.etat_visit:
                tableau.append(EtatCas2(self.tg, self.etat_visit.copy(), adjacent, self.etat_debut))

        return tableau

    def h(self):
        # Heuristique basée sur le nombre d'états restants à visiter et le poids minimum entre les états sur terre
        return (self.tg.getNbSommets() - len(self.etat_visit)) * self.tg.getPoidsMinTerre()

    def k(self, e):
        # Coût entre l'état courant et l'état e
        return self.tg.getCoutArete(self.etat_courant, e.etat_courant)

    def displayPath(self, _):
        # Affiche les états visités dans l'ordre
        print("sur", self.tg.getNbSommets(), "villes :", self.etat_visit)

    # METHODES pour pouvoir utiliser cet objet dans des listes et des map
    def __hash__(self):
        # Utilise un tuple pour générer un hash basé sur les états visités
        # Dans le cas du EtatCas2, les états visités sont stockés dans une liste, et les listes en Python ne sont pas hashables 
        # parce qu'elles sont mutables (leur contenu peut être modifié après la création). 
        # Cependant, les tuples sont immuables, ce qui signifie que leur contenu ne peut pas être modifié après leur création. 
        # La conversion en tuple dans la fonction __hash__ est une manière de contourner cette limitation. 
        # En convertissant la liste d'états visités en un tuple (qui est hashable), on peut utiliser cette 
        # valeur comme clé dans un dictionnaire ou comme élément dans un ensemble.
        return hash(tuple(self.etat_visit))

    def __eq__(self, o):
        # Compare les états visités pour vérifier l'égalité
        return self.etat_courant == o

    # METHODES pour affichage futur (héritée d'Object)
    def __str__(self):
        # Affiche les états visités sous forme de chaîne de caractères
        return " ".join(str(etat) for etat in self.etat_visit)