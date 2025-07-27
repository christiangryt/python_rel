import heapq
import math
from collections import defaultdict
# TODO:chatGPT løsning enn så lenge
import itertools

def astar(start, end, graph, state = None):
    """
    astar with simple "Manhatten Diagonal" heuristic
    node class objects as start and stop
    and graph class object
    if state, treats other states as *
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
                open = []

                neigh.parent = q

                while q != start:

                    # To represent the path
                    # TODO: Make toggleble. This is purely aestetic
                    q.state = start.state.lower()

                    path.append(q)

                    #print (neigh.parent)
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
        if self.state == "*":
            return " "
        else:
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
                    res.neighbors.remove(self)

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

            self.nodes.append(node (
                y,
                x,
                n
            ))

            if n != "." and n != "*":
                self.terminals[n].append((y,x))

        # Dictionary on coord tuple
        self.node_locations = {
                (n.y, n.x) : n for n in self.nodes
            }

        self.add_all_neighbors()


    def display_graph(self, state=False, parent=False):
        # Plan is to make have different "filters" to display information

        # TODO: Format better
        counter = 0
        for i in range(math.ceil(len(self.nodes) / self.width)):
            print (self.nodes[counter:counter+self.width])
            counter += self.width

    def set_neighbors(self, conditions):
        """
        Attempts to remove all neighbors from given positions
        Lets terminals have a local environment
        """

        for c in conditions:

            node = self.node_locations.get(c)
            node.find_neighbors(
                    self.node_locations,
                    delete = True
                )

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

    def add_all_neighbors(self):

        for n in self.nodes:
            n.find_neighbors(
                    self.node_locations
                )

class flow():
    """
    Plan for self:
    Represent a color (A->A). Calls path finding, this should be abstracted to more easily change the heuristics

    (This pathfinding needs to be easily able to respect the restrictions given by the CBS. I do have to solve it several times, but alas)
    """

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
        "A", ".", ".", ".", "B",
        ".", "*", ".", ".", ".",
        "*", "*", ".", ".", ".",
        ".", ".", ".", ".", ".",
        "A", "*", "B", ".", ".",
    ]
]

# Make graph object
g = graph(test2)

start = g.node_locations.get(g.terminals["A"][0])
end = g.node_locations.get(g.terminals["A"][1])

g.set_neighbors(g.terminals["B"])

path = astar(start, end, g)

g.add_all_neighbors()
g.set_neighbors(g.terminals["A"])
start = g.node_locations.get(g.terminals["B"][0])
end = g.node_locations.get(g.terminals["B"][1])

path = astar(start,end, g)

g.display_graph()
print (g.terminals)

# Saving all terminals, i can easily change their state to * for other terminal colors such that they appear as not in play
# Either: Make a copy of the board so i can change states and maka truly local board
# Or: Check the state of squares i investigate and whether or not they are valid for my starting state

# works. if i want to ill optimize to not check already found neighbors, but, i
# dont think it will affect it in the long run
# As of now, it prefers routes on the outside, i believe this is due to the tie breaker
