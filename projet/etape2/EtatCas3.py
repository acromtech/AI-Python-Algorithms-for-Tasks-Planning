from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat

class EtatCas3(Etat):
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

        # Si tous les états ont été visités, crée un état supplémentaire pour revenir au point de départ
        if len(self.etat_visit) == self.tg.getNbSommets():
            return [EtatCas3(self.tg, self.etat_visit.copy(), self.etat_debut, self.etat_debut)]

        # Ajoute tous les sommets non visités dans le tableau (pas de condition supplémentaire ici par rapport au cas 2)
        for sommet in self.tg.getSommets():
            if sommet not in self.etat_visit:
                tableau.append(EtatCas3(self.tg, self.etat_visit.copy(), sommet, self.etat_debut))

        return tableau

    def h(self):
        # Heuristique basée sur le nombre d'états restants à visiter et le poids minimum dans les airs
        return (self.tg.getNbSommets() - len(self.etat_visit)) * self.tg.getPoidsMinAir()

    def k(self, e):
        # Coût entre l'état courant et l'état e, calculé en utilisant la distance entre les états
        return GrapheDeLieux.dist(self.etat_courant, e.etat_courant, self.tg)

    def displayPath(self):
        # Affiche le chemin trouvé en utilisant une flèche pour représenter les déplacements entre les états
        print("Le chemin trouvé est : ")
        print(" >>>>> ".join(str(etat) for etat in self.etat_visit))

    # METHODES pour pouvoir utiliser cet objet dans des listes et des map
    def __hash__(self):
        # Utilise un tuple pour générer un hash basé sur le graphe, l'état courant et les états visités
        return hash((self.tg,self.etat_courant, tuple(self.etat_visit)))

    def __eq__(self, o):
        # Compare les états visités pour vérifier l'égalité
        return self.etat_visit == o

    # METHODES pour affichage futur (héritée d'Object)
    def __str__(self):
        # Affiche les états visités sous forme de chaîne de caractères
        return " ".join(str(etat) for etat in self.etat_visit)
