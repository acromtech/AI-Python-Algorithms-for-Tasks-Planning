from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.solvers.SolverCSP import SolverCSP

class Etape4 :

    if __name__ == '__main__':

        print("\n========== TEST  ==========")
        print("=============================")

        #    TEST 1 : town10.txt avec 3 couleurs
        tg : GrapheDeLieux = GrapheDeLieux.loadGraph("Data/town10.txt",True)
        print("\nTest sur town10 avec 3 couleurs (on attend OK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 3)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(True)

        #    TEST 2 : town10.txt avec 2 couleurs
        print("\nTest sur town10 avec 2 couleurs (on attend NOK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 2)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(False)

        #    TEST 3 : town10.txt avec 4 couleurs
        print("\nTest sur town10 avec 4 couleurs (on attend OK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 4)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(False)

        #    TEST 4 : flat20_3_0.col avec 4 couleurs
        tg = GrapheDeLieux.loadGraph("Data/pb-etape1/flat20_3_0.col",False)
        print("Test sur flat20_3_0.col avec 4 couleurs (on attend OK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 4)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(False)

        #    TEST 5 : flat20_3_0.col avec 3 couleurs
        print("Test sur flat20_3_0.col avec 3 couleurs (on attend OK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 3)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(False)

        #    TEST 6 : flat20_3_0.col avec 2 couleurs
        print("Test sur flat20_3_0.col avec 2 couleurs (on attend NOK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 2)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(False)

        #    TEST 7 : jean.col avec 10 couleurs
        tg = GrapheDeLieux.loadGraph("Data/pb-etape1/jean.col",False)
        print("Test sur jean.col avec 10 couleurs (on attend OK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 10)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(False)

        #    TEST 9 : jean.col avec 3 couleurs
        print("Test sur jean.col avec 3 couleurs (on attend NOK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        solver = SolverCSP(tg, 3)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        solver.solve(False)

        #    TEST 8 : jean.col avec 9 couleurs
        #print("Test sur jean.col avec 9 couleurs (on attend NOK) :")
        # Créez une instance du solver CSP avec le graphe et le nombre de couleurs souhaité
        #solver = SolverCSP(tg, 9)
        # Résolvez le problème (complet=True pour obtenir toutes les solutions)
        #solver.solve(False)
