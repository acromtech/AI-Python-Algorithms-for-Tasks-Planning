from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.solvers.SolverAStar import SolverAStar

from projet.etape2.EtatCas1 import EtatCas1
from projet.etape2.EtatCas2 import EtatCas2
from projet.etape2.EtatCas3 import EtatCas3

class Etape2 :
    tg = GrapheDeLieux.loadGraph("Data/town10.txt",True)
    cas1 = EtatCas1(tg,0,9)
    SolverAStar.aStar(cas1)

    cas1 = EtatCas1(tg,5,9)
    SolverAStar.aStar(cas1)

    cas1 = EtatCas1(tg,2,9)
    SolverAStar.aStar(cas1)

    cas1 = EtatCas1(tg,1,7)
    SolverAStar.aStar(cas1)

    tg = GrapheDeLieux.loadGraph("Data/town30.txt",True)
    cas1 = EtatCas1(tg,0,25)
    SolverAStar.aStar(cas1)

    tg = GrapheDeLieux.loadGraph("Data/town150.txt",True)
    cas1 = EtatCas1(tg,0,145)
    SolverAStar.aStar(cas1)

    tg = GrapheDeLieux.loadGraph("Data/town1000.txt",True)
    cas1 = EtatCas1(tg,0,997)
    SolverAStar.aStar(cas1)

    # CAS 2 : tour complet par voie de terre
    #tg = GrapheDeLieux.loadGraph("Data/town10.txt", True)
    #cas2 = EtatCas2(tg)
    #SolverAStar.aStar(cas2)

    # CAS 3 : tour complet par voie des airs // Utilisation de la fonction aStarOpti car chargement très gourmant en ressources
    #tg = GrapheDeLieux.loadGraph("Data/town6.txt",True)
    #cas3 = EtatCas3(tg)
    #SolverAStar.aStarOpti(cas3)

    # tg = GrapheDeLieux.loadGraph("Data/town7.txt",True)
    # cas3 = EtatCas3(tg)
    # SolverAStar.aStarOpti(cas3)

    # tg = GrapheDeLieux.loadGraph("Data/town8.txt",True)
    # cas3 = EtatCas3(tg)
    # SolverAStar.aStarOpti(cas3)

    # tg = GrapheDeLieux.loadGraph("Data/town9.txt",True)
    # cas3 = EtatCas3(tg)
    # SolverAStar.aStarOpti(cas3)

    # tg = GrapheDeLieux.loadGraph("Data/town10.txt",True)
    # cas3 = EtatCas3(tg)
    # SolverAStar.aStarOpti(cas3)

    # tg = GrapheDeLieux.loadGraph("Data/town11.txt",True)
    # cas3 = EtatCas3(tg)
    # SolverAStar.aStarOpti(cas3)
                                                                                                            

