from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.Solution import Solution
import random

class UneSolution(Solution): # Classe pour définir une solution pour le cas 3 de la tâche 2 (hérite de Solution)
    # attributs
    tg: GrapheDeLieux
    """ le graphe représentant le monde """

    # constructeurs
    def __init__(self, tg: GrapheDeLieux, cycle=None):
        """ constructeur d'une solution à partir du graphe représentant le monde
        :param tg: graphe représentant le monde """
        self.tg = tg

        if cycle==None:
            self.cycle=[i for i in range(self.tg.getNbSommets())]
            random.shuffle(self.cycle)
            self.cycle.append(self.cycle[0])
        else:
            self.cycle=cycle

    # méthodes de la classe abstraite Solution
    def lesVoisins(self):
        """ méthode récupérant la liste des voisins de la solution courante
        :return liste des voisins de la solution courant"""
        voisin=[]
        list_i=[]
        for i in range(self.tg.getNbSommets()-1):
            index=random.randint(1,self.tg.getNbSommets()-1)
            index2=random.randint(index+1,self.tg.getNbSommets())
            while index in list_i:
                index=random.randint(1,self.tg.getNbSommets()-1)
                index2=random.randint(index+1,self.tg.getNbSommets())
            list_i.append(index)
            nouveau_cycle=self.cycle[0:index] + self.cycle[index2-1:index-1:-1] + self.cycle[index2:]
            voisin.append(UneSolution(self.tg,nouveau_cycle))
        return voisin

    def unVoisin(self):
        """methode recuperant un voisin de la solution courante
        :return voisin de la solution courante"""
        return [self.lesVoisins()[0]]

    def eval(self):
        """ méthode récupérant la valeur de la solution courante
        :return valeur de la solution courante """
        val=0
        for i in range(len(self.cycle)-1):
            etat1=self.cycle[i]
            etat2=self.cycle[i+1]
            val+=GrapheDeLieux.dist(etat1,etat2,self.tg)
        return val

    def nelleSolution(self):
        """ méthode générant aléatoirement une nouvelle solution à partir de la solution courante
        :return nouvelle solution générée aléatoirement à partir de la solution courante"""
        cycle=[i for i in range(self.tg.getNbSommets())]
        random.shuffle(cycle)
        new_cycle=cycle+[cycle[0]]
        return UneSolution(self.tg,new_cycle)

    def displayPath(self):
        """ méthode affichant la solution courante comme un chemin dans le graphe """
        print("la solution courante : ",self.eval(),"\n",self.cycle,"\n")

    # méthodes pour pouvoir utiliser cet objet dans des listes et des map
    def __hash__(self):
        """ méthode permettant de récupérer le code de hachage de la solution courante
        pour une utilisation dans des tables de hachage
        :return code de hachage"""
        return hash(self.cycle)

    def __eq__(self, o):
        """ méthode de comparaison de la solution courante avec l'objet o
        :param o: l'objet avec lequel on compare
        :return True si la solution courante et o sont égaux, False sinon"""
        return self.eval == o

    # méthode pour affichage futur (héritée d'Object)
    def __str__(self):
        """ méthode mettant la solution courante sous la forme d'une
        chaîne de caractères en prévision d'un futur affichage
        :return représentation de la solution courante sous la forme d'une chaîne de caractère"""
        path_str = "Le chemin optimal est : " + " -> ".join(str(sommet) for sommet in self.cycle)
        return f"{path_str}\nLa meilleure solution a une valeur de {self.eval()}"
