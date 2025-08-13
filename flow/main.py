from cbs import *

# first element row width and the rest is flattened data
test = [
    3,
    [
        "A", ".", "A",
        "*", "B", ".",
        "*", "*", "B"
    ],
]

test2 = [
    5,
    [
        "A", "D", ".", ".", "D",
        ".", "C", "*", "C", "B",
        ".", ".", "*", ".", ".",
        ".", ".", "*", ".", ".",
        ".", ".", "*", ".", ".",
        ".", ".", "*", ".", ".",
        ".", ".", "*", ".", ".",
        ".", ".", "*", ".", ".",
        ".", ".", "*", ".", ".",
        ".", ".", ".", ".", ".",
        ".", "E", "*", "E", ".",
        ".", ".", "*", ".", ".",
        "A", ".", ".", ".", "B",
    ]
]

easy = [
    5,
    [
        "D", ".", ".", ".", ".",
        ".", ".", ".", ".", ".",
        ".", ".", "B", ".", ".",
        "C", "B", "A", ".", "D",
        "A", ".", ".", ".", "C",
    ]
]

medium = [
    7,
    [
        ".", ".", ".", ".", "A", ".", ".",
        ".", "B", ".", ".", ".", "C", ".",
        ".", "C", ".", ".", ".", "B", ".",
        ".", "A", "D", ".", ".", ".", ".",
        ".", "D", "E", ".", "E", ".", ".",
        ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".",
    ]
]

coll = [
    5,
    [
        "B", "*", "C", "B", ".",
        ".", ".", ".", ".", ".",
        "A", "*", ".", ".", ".",
        "*", "A", ".", ".", "C",
    ]
]

less_hard = [
    8,
    [
        "E", "C", "F", ".", ".", ".", ".", ".",
        ".", ".", "B", "D", ".", "A", ".", ".",
        ".", ".", ".", "B", ".", "E", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "C", ".", ".", ".",
        ".", ".", "D", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", "F", "A", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
    ]
]

hard = [
    8,
    [
        ".", "D", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "D", ".", ".", ".",
        ".", ".", ".", "C", ".", ".", ".", ".",
        ".", ".", ".", "A", ".", ".", ".", ".",
        ".", ".", "B", ".", ".", ".", ".", ".",
        ".", "C", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", "A", ".", "B",
    ]
]

simple = [
    4,
    [
        "A", ".", ".", ".",
        "B", ".", "B", ".",
        "A", ".", ".", ".",
    ]
]

# Make graph object
g = graph(less_hard)

# Solver
cbs = CBS_solver(g)

cbs.solve_puzzle()

# Saving all terminals, i can easily change their state to * for other terminal colors such that they appear as not in play
# Either: Make a copy of the board so i can change states and maka truly local board
# Or: Check the state of squares i investigate and whether or not they are valid for my starting state

# works. if i want to ill optimize to not check already found neighbors, but, i
# dont think it will affect it in the long run
# As of now, it prefers routes on the outside, i believe this is due to the tie breaker
