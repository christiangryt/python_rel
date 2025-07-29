import heapq
import math
from collections import defaultdict
# TODO:chatGPT løsning enn så lenge
import itertools

def astar(start, end, graph):
    """
    astar with simple "Manhatten Diagonal" heuristic
    node class objects as start and stop
    and graph class object
    """

    graph.reset_astar_values()

    #TODO: Make this prettier
    start.f = 0
    start.g = 0
    start.h = 0

    counter = itertools.count()

    open = []
    closed = []

    # add starting node to open heap
    heapq.heappush(open, (start.f, next(counter), start))

    while open:
        # litt janky, men trenger ikke pri
        q = heapq.heappop(open)[-1]

        for neigh in q.neighbors:
            #print (f"looking at {neigh}")
            if neigh == end:
                # returner nodene denne er innom
                # loop gjennom parents
                print ("Found exit")
                path = []

                neigh.parent = q

                while q != start:
                    path.append(q)
                    q = q.parent

                return path

            g = q.g + 1
            h = abs(neigh.x - end.x) + abs(neigh.y - end.y)
            f = g + h

            if f < neigh.f :
                heapq.heappush(open, (neigh.f, next(counter), neigh))

                neigh.f = f
                neigh.h = h
                neigh.g = g

                # TODO: Make this prettier in a way
                neigh.parent = q
                q.successor.append(neigh)

                # Visualize moves made by algorithm
                #q.state = start.state.lower()

        # Visualize
        #print (graph.display_graph())

class node():

    def __init__(self, y, x, state):

        self.state = state

        self.y = y
        self.x = x

        self.f = 0 # Total cost
        self.g = 0 # Cost to node from start
        self.h = 0 # Heuristic cost estimate

        self.neighbors = []
        self.parent = None
        self.successor = []

    def __repr__(self):
        return f"{self.state}"
        #return f"Node at ({self.y},{self.x})"

    def find_neighbors(self, d, delete = False):
        """
        Given dictionary of nodes that exist, adds or deletes neighbors
        """

        search = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        #print ("---")
        #print (self)
        for s in search:

            new_y = self.y + s[1]
            new_x = self.x + s[0]
            #print (f"{new_y} {new_x}")

            res = d.get((new_y, new_x))
            #print (res)

            if res:

                if not delete:
                    # TODO: Make not ugly
                    if res.state != "*":
                        self.neighbors.append(res)

                else:
                    try:
                        res.neighbors.remove(self)
                    except:
                        None

class graph():

    def __init__(self, graph):
        """
        Given nested list like, f.ex.
        Where . is an empty square and * is not in use
        (I think passing a tuple/list where [0] is the length of each row and [1] being the flattened data. Easier to work with, and i can later make something to convert this below to said flattened structure)

        [
            3,
            ["A", ".", "A","*", "B", ".","*", "*", "B"],
        ]

        Make node objects with correct neighbors and  states
        Will also store location of terminals (any other symbol than . or *)
        """

        self.width = graph[0]
        self.nodes = []
        self.terminals = defaultdict(list)

        # Make nodes if square is in play
        for i,n in enumerate(graph[1]):

            y = i // self.width
            x = i % self.width

            nnode = node(y, x, n)
            self.nodes.append(nnode)

            if n != "." and n != "*":
                self.terminals[n].append(nnode)

        # Dictionary on coord tuple
        self.node_locations = {
                (n.y, n.x) : n for n in self.nodes
            }

        # TODO: Add function to add neighbors to only some nodes. I.e. redo neighbors without redoing entire grid
        self.add_neighbors()


    def display_graph(self, state=False, parent=False):
        # Plan is to make have different "filters" to display information

        # TODO: Format better
        counter = 0
        for i in range(math.ceil(len(self.nodes) / self.width)):
            print (self.nodes[counter:counter+self.width])
            counter += self.width

    def set_neighbors(self, conditions):
        """
        Attempts to remove all neighbors from given nodes
        Lets terminals have a local environment
        """

        for c in conditions:

            c.find_neighbors(
                    self.node_locations,
                    delete = True
                )
            c.neighbors = []

    def reset_astar_values(self):
        """
        Reset attr. to none and inf
        Unsure if this is best practice, but seeing as im going to have to run a* one million times...
        """

        for n in self.nodes:
            n.f = float("inf")
            n.g = float("inf")
            n.h = float("inf")

            n.parent = None
            n.successor = []

    def add_neighbors(self, nodes = None):

        # TODO: If performance issues, this function might be part of it
        checked = []

        if not nodes:
            nodes = self.nodes

        for n in nodes:

            checked.append(n)

            n.find_neighbors(
                    self.node_locations
                )
            for neigh in n.neighbors:

                if neigh in checked:
                    continue

                neigh.find_neighbors(
                    self.node_locations
                )

class flow():
    """
    Plan for self:
    Represent a color (A->A). Calls path finding, this should be abstracted to more easily change the heuristics

    (This pathfinding needs to be easily able to respect the restrictions given by the CBS. I do have to solve it several times, but alas)
    """

    def __init__(self, graph):
        """
        Graph object (list of nodes with neighbors)
        """

        self.graph = graph

        # Each terminal and their restrictions
        self.conditions = defaultdict(list)

        for term in self.graph.terminals:

            all_terms = self.graph.terminals.values()

    def solve_terminals(self):
        None

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
        ".", ".", ".", ".", ".",
        ".", "E", "*", "E", ".",
        ".", ".", "*", ".", ".",
        "A", ".", ".", ".", "B",
    ]
]

# Make graph object
g = graph(test2)

# List of solutions
sol = []

# Construct list of terminals except current
# By concatinating the lists not appending (make one long list not nested list)
all_terminals = []
for s,t in g.terminals.items():
    all_terminals += t

# Visual representation of all paths
# Encorporate this to show each iteration?
for state, term in g.terminals.items():

    start = g.terminals[state][0]
    end = g.terminals[state][1]

    # Terminal nodes without current terminals
    exclude = [x for x in all_terminals if x not in term]

    # Reset board to previous state and remove 
    # (If abnormalities with board state and solutions, maybe something has broken here)
    ### Funny quirk, add_neighbors THEN set_neighbors (bad logic)
    g.add_neighbors(all_terminals)
    g.set_neighbors(exclude)

    # Solve and save
    path = astar(start, end, g)
    sol.append((start.state, path))

# Purely aestetic. Wrap into grap function or smth
for s in sol:
    for n in s[1]:
        n.state = s[0].lower()

g.display_graph()

# Saving all terminals, i can easily change their state to * for other terminal colors such that they appear as not in play
# Either: Make a copy of the board so i can change states and maka truly local board
# Or: Check the state of squares i investigate and whether or not they are valid for my starting state

# works. if i want to ill optimize to not check already found neighbors, but, i
# dont think it will affect it in the long run
# As of now, it prefers routes on the outside, i believe this is due to the tie breaker
