from cbs import *
from boards import *

# Make graph object
g = graph(less_hard)

# Solver
cbs = CBS_solver(g)

cbs.solve_puzzle()
