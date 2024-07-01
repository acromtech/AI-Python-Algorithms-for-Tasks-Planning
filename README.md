# AI Algorithms on Linux

## Context

Our robot, R2D2, operates in a 2D world represented by an undirected graph. The graph's edges denote paths R2D2 can take, and the nodes represent locations where R2D2 must perform tasks. Each edge is weighted to represent the path's length, and each node is weighted by its position in the 2D plane.

R2D2's mission is to place a colored cube at each location such that neighboring locations (connected by an edge) have different colored cubes. Three main tasks have been identified.

## Project Planning

The project is divided into 5 stages over 12 lab sessions.

1. **Stage 1 (Sessions 1 and 2):** Solve Task 1 - Use propositional logic to determine if three colors are sufficient, utilizing a SAT solver.

2. **Stage 2 (Sessions 3 to 6):** Solve Task 2 - Calculate the shortest paths between locations, addressing three cases with different algorithms.
    - **Case 1:** Shortest path between two locations using distances and Cartesian coordinates.
    - **Case 2:** Shortest path visiting each location once and returning to the starting point.
    - **Case 3:** Incorporate R2D2's flying capability, allowing straight-line travel between locations.

3. **Stage 3 (Sessions 7 and 8):** Continue Task 2 - Optimize methods to calculate less optimal but faster paths.

4. **Stage 4 (Sessions 9 and 10):** Solve Task 3 - Use a constraint graph to determine the minimum number of colors needed.

5. **Stage 5 (Sessions 11 and 12):** Continue Task 2 - Solve Case 3 of Task 2 by formulating the problem using mathematical expressions (using ZIMPL and SCIP).

**Important Note for Stage 5:** All ZIMPL programs are stored in separate `town(n).zpl` files, and results are displayed in separate `log(n)` files, where `n` corresponds to the number of towns. Ensure your software library paths are correctly set for proper functioning:

```python
# Path to libtbb.so.2
tbb_path = '/snap/blender/4300/lib'

# Add the path to LD_LIBRARY_PATH
os.environ['LD_LIBRARY_PATH'] = f"{tbb_path}:{os.environ.get('LD_LIBRARY_PATH', '')}"
```

## Running the Program

1. **Navigate to the repository directory after downloading.**
```bash
cd [path/to/repository]
```
2. **Run the program.**
```bash
make all
```
3. **Results are displayed in the `log` file next to the Makefile.**

## Dependencies

When running the program (`make all`), it will check for the required dependencies and **automatically install them** if missing:
- python-sat
- python-constraint
- libopenblas-base
- libtbb-dev

## Project Structure
```
.
├── Data
│   ├── pb-etape1
│   │   ├── (...)
│   ├── pb-etape5
│   │   ├── tsp10.txt
│   │   ├── tsp11.txt
│   │   ├── tsp12.txt
│   │   ├── tsp13.txt
│   │   ├── tsp146.txt
│   │   ├── tsp14.txt
│   │   ├── tsp15.txt
│   │   ├── tsp16.txt
│   │   ├── tsp17.txt
│   │   ├── tsp18.txt
│   │   ├── tsp19.txt
│   │   ├── tsp26.txt
│   │   ├── tsp6.txt
│   │   ├── tsp7.txt
│   │   ├── tsp8.txt
│   │   ├── tsp998.txt
│   │   └── tsp9.txt
│   ├── town1000.txt
│   ├── town10.txt
│   ├── town11.txt
│   ├── town12.txt
│   ├── town13.txt
│   ├── town14.txt
│   ├── town150.txt
│   ├── town15.txt
│   ├── town16.txt
│   ├── town17.txt
│   ├── town18.txt
│   ├── town19.txt
│   ├── town30.txt
│   ├── town6.txt
│   ├── town7.txt
│   ├── town8.txt
│   └── town9.txt
├── Doc
│   ├── projet
│   │   ├── etape1
│   │   ├── etape2
│   │   ├── etape3
│   │   ├── etape4
│   │   ├── index.html
│   │   ├── outils
│   │   └── solvers
│   └── SCIP
│       ├── README-doc-SCIP
│       └── zimpl-docSimplifiee.pdf
├── log
├── Makefile
├── projet
│   ├── etape1
│   │   ├── Etape1.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── etape2
│   │   ├── Etape2.py
│   │   ├── EtatCas1.py
│   │   ├── EtatCas2.py
│   │   ├── EtatCas3.py
│   │   ├── Etat.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── etape3
│   │   ├── Etape3.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── Solution.py
│   │   └── UneSolution.py
│   ├── etape4
│   │   ├── Etape4.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── etape5
│   │   ├── Etape5.py
│   ├── __init__.py
│   ├── outils
│   │   ├── Fils.py
│   │   ├── GrapheDeLieux.py
│   │   ├── __init__.py
│   │   ├── Lieu.py
│   │   └── __pycache__
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── solvers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── SCIP
│   │   ├── SCIP.zip
│   │   ├── SolverAStar.py
│   │   ├── SolverCSP.py
│   │   ├── SolverHC.py
│   │   ├── SolverSAT.py
│   │   └── SolverTabou.py
│   └── tests
│       └── logReference
└── README.md
```
