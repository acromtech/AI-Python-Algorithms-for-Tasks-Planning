from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.solvers.SolverSAT import SolverSAT

class Etape1:
    # ATTRIBUTS
    g: GrapheDeLieux  # Le graphe représentant le monde
    base: list  # La base de clauses représentant le problème.
    # C'est une liste de listes d'entiers, un entier par variable
    # (positif si littéral positif, négatif sinon).
    # Notez que 0 n'est pas autorisé pour représenter une variable (mis à jour par updateBase)
    nbVariables: int  # Le nombre de variables utilisées pour représenter le problème (mis à jour par updateBase)

    # CONSTRUCTEUR
    def __init__(self, fn: str, form: bool):
        # :param fn: le nom du fichier contenant les sommets et les arêtes
        # :param form: utilisé pour distinguer différents types de fichiers
        # (pour ceux contenant des poids et des coordonnées, form est True ; pour les autres, form est False)

        self.g = GrapheDeLieux.loadGraph(fn, form)
        self.base = []  # Base (liste des arêtes + liste des noeuds + liste des couleurs)
        self.color = []  # Liste des possibilités de couleur
        self.node = []  # Liste des possibilités de couleur pour chaque noeud
        self.edge = []  # Liste des contraintes (arêtes du graphe / liens entre les noeuds)
        self.nbVariables = 0  # Nombre initial de couleurs

        # Mettre les listes en listes triées
        self.color.sort()
        self.node.sort()
        self.edge.sort()

    # METHODES
    def updateBase(self, x: int):  # Méthode pour mettre à jour la base de clauses et le nombre de variables en fonction du problème à résoudre
        # Initialisation
        self.base.clear()
        self.color.clear()
        self.node.clear()
        self.edge.clear()
        self.nbVariables = x * (self.g.getNbSommets())

        # Configurer les choix de couleur possibles pour chaque état du graphe
        # Exemple : pour 3 couleurs et un état donné, on aura (1001, 1002, 1003)
        # Exemple : pour 4 couleurs et 2 états donnés, on aura (1001, 1002, 1003, 1004), (2001, 2002, 2003, 2004)
        for node in range(self.g.getNbSommets()):  # Pour tous les états du graphe
            for color in range(x):  # Pour toutes les couleurs
                self.color.extend([(color + 1) + 1000 * (node + 1)])  # Stocker toutes les possibilités de couleur (jusqu'à 999 couleurs)
                for edge in self.g.getAdjacents(node):  # Pour toutes les arêtes du noeud
                    if (1000 + (color + 1) + 1000 * node) != ((edge + 1) * 1000 + (color + 1)):  # Si ce n'est pas le même noeud
                        self.edge.append([-(1000 + (color + 1) + 1000 * node),
                                          -((edge + 1) * 1000 + (color + 1))])  # Ajouter la contrainte de couleur à la liste des arêtes pour le noeud

            self.node.append(self.color)  # Stocker dans une nouvelle liste pour tous les noeuds
            self.color = []  # Vider la liste de couleurs pour la prochaine fois

        # Inclure les contraintes de noeud, d'arête et de couleur dans la liste de base
        self.base.extend(self.node)  # Remplir la base avec la liste des noeuds
        self.base.extend(self.edge)  # Remplir la base avec la liste des arêtes

    def runSolver(self):  # Méthode pour appeler le solveur sur la base de clauses représentant le problème
        return SolverSAT.solve(self.base)  # :return True si la base de clauses représentant le problème est satisfaisante, False sinon

    def displayBase(self):  # Afficher la base de clauses représentant le problème
        print('Base de clause utilise ', self.nbVariables, ' variables et contient les clauses suivantes :')
        for clause in self.base:
            print(clause)


class __testEtape1__:
    # TESTS
    if __name__ == '__main__':
        step = Etape1("Data/town10.txt", True)
        step.updateBase(3)
        print("town10 avec 3 couleurs (attendu True) : ", step.runSolver())
        step.displayBase()
        step.updateBase(2)
        print("town10 avec 2 couleurs (attendu False) : ", step.runSolver())
        step.updateBase(4)
        print("town10 avec 4 couleurs (attendu True) : ", step.runSolver())

        step = Etape1("Data/pb-etape1/flat20_3_0.col", False)
        step.updateBase(4)
        print("flat20_3_0.col avec 4 couleurs (attendu True) : ", step.runSolver())
        step.updateBase(3)
        print("flat20_3_0.col avec 3 couleurs (attendu True) : ", step.runSolver())
        step.updateBase(2)
        print("flat20_3_0.col avec 2 couleurs (attendu False) : ", step.runSolver())

        step = Etape1("Data/pb-etape1/jean.col", False)
        step.updateBase(10)
        print("jean.col avec 10 couleurs (attendu True) : ", step.runSolver())
        step.updateBase(9)
        print("jean.col avec 9 couleurs (attendu False) : ", step.runSolver())
        step.updateBase(3)
        print("jean.col avec 3 couleurs (attendu False) : ", step.runSolver())
