import heapq
import math
from collections import defaultdict
# TODO:chatGPT løsning enn så lenge
import itertools

def astar(start, end, graph, constraints):
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
                #print ("Found exit")
                path = []

                neigh.parent = q

                while q != start:
                    path.append(q)
                    q = q.parent

                return path

            elif neigh not in constraints:

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

    # If no path return empty list
    return []

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

        for s in search:

            new_y = self.y + s[1]
            new_x = self.x + s[0]

            res = d.get((new_y, new_x))

            if res:

                if delete == False:
                    # TODO: Make not ugly and if in check is needed
                    if res.state != "*" and res not in self.neighbors:
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

            # TODO: Perhaps change to better name
            nnode = node(y, x, n)
            self.nodes.append(nnode)

            if n != "." and n != "*":
                self.terminals[n].append(nnode)

        # Dictionary on coord tuple
        self.node_locations = {
                (n.y, n.x) : n for n in self.nodes
            }

        self.add_neighbors()

        # By concatinating the lists not appending (make one long list not nested list)
        self.all_terminals = []
        for t in self.terminals.values():
            self.all_terminals += t

    def reset_node_states(self):
        """
        Sets states to default symbol ".". keeps terminals same state
        """

        for node in self.nodes:
            if node not in self.all_terminals and node.state != "*":
                node.state = "."

    def display_graph(self, paths_alone=False):
        # TODO: Format better
        counter = 0

        for i in range(math.ceil(len(self.nodes) / self.width)):
            print (self.nodes[counter:counter+self.width])
            counter += self.width

    def set_neighbors(self, conditions):
        """
        Attempts to remove all neighbors from given nodes
        Lets terminals have a local environment

        I.e. it is a node, context comes from what calls function
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
        # TODO: Solve how to re-add all restrictions
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

class cbs_node():

    def __init__(self, constraints):

        self.constraints = constraints

class flow():
    """
    Plan for self:
    Represent a color (A->A). Calls path finding, this should be abstracted to more easily change the heuristics

    (This pathfinding needs to be easily able to respect the restrictions given by the CBS. I do have to solve it several times, but alas)
    """

    def __init__(self, graph, terminals, state):
        """
        Graph object (list of nodes with neighbors)
        """

        self.graph = graph
        self.state = state              # Symbol for Terminals
        self.terminals = terminals
        self.path = []              # My way of storing the solution, might need a looker

        # Terminal nodes without these terminals
        self.exclude = set([x for x in self.graph.all_terminals if x not in self.terminals])

        # Nodes not available to flow. Will be changed by CBS_nodes
        self.constraints = set(self.exclude)

    def set_constraint(self, constraints):
        """
        Adds new constraints while keeping terminals part of list
        """

        self.constraints = constraints.union(self.exclude)

    def solve_terminal(self):
        """
        Solve Flow with state of graph
        """

        start, end = self.terminals

        ### Funny quirk, add_neighbors THEN set_neighbors (bad logic)
        # Good idea, remove constraint nodes, then add them back in the same function. clean slate for next flow
        # TODO: Fix reference to graph. Pain to reference self.graph and then whatever
        print(f"{self.state} : {[(x.y, x.x, x.state) for x in self.constraints]}")

        #self.graph.set_neighbors(self.constraints)
        #print (self.constraints)

        if self.state == "B":
            print (self.graph.node_locations[(2,1)].neighbors)

        # TODO: Add potential to easily change path finding
        self.path = astar(start, end, g, self.constraints)

        #self.graph.add_neighbors()

class CBS_solver(graph):
    """
    Note to self, this is the object that should make CBS_nodes and handle solving.
    Flow class keeps track of a single path, this keeps track of all tracks
    """

    def __init__(self, graph):

        self.flows = []
        self.graph = graph

        # First make flow objects from all_terminals list
        for state, nodes in self.graph.terminals.items():
            self.flows.append(flow(self.graph, nodes, state))

    def set_constraints(self, constraints):
        for flow in self.flows:
            flow.set_constraint(constraints[flow.state])

    def amount_constraints(self, constraints):

        ut = []
        #print (constraints)

        for con in constraints.values():
            ut += con

        return len(ut)

    def solve_terminals(self):

        for flow in self.flows:
            flow.solve_terminal()

    def find_first_conflict(self):
        """
        Finds approximation to error with no prior error based on distance to terminals
        """

        # Flow and path index
        usage = defaultdict(list)

        # Might be ugly and stupid
        for flow in self.flows:

            path_length = len(flow.path)
            if path_length == 0:
                return False

            for node_index, node in enumerate(flow.path):
                distance_from_terminal = min(node_index, path_length - node_index - 1)
                usage[node].append((flow, distance_from_terminal))

        conflicts = defaultdict(list)
        for node, locs in usage.items():
            if len(locs) > 1:
                flows = [x[0] for x in locs]
                avg_dist_terminal = sum([x[1] for x in locs]) / len(locs)
                conflicts[avg_dist_terminal].append((node,flows))

        #print (conflicts[min(conflicts.keys())][0])

        # TODO: Return first, find more elegent later (that cares for path length or smth)
        try:
            return conflicts[min(conflicts.keys())]
        except:
            return True

    def solve_puzzle(self):

        # Flow + list of constraints
        #constraints = defaultdict(list)
        constraints = defaultdict(set)

        # TODO: Implement Board Fill heuristic
        cost = None
        constraint_cost = self.amount_constraints(constraints)
        counter = itertools.count()

        root = cbs_node(constraints)

        # Solutions to check
        open = []
        heapq.heappush(open, (constraint_cost, next(counter), root))

        while open:
        #for i in range (10):

            print ("---")

            # Least constraints
            P = heapq.heappop(open)[-1]
            constraints = P.constraints

            # DEBUG
            for state, con in constraints.items():
                print (f"{state}: {*[(x.y,x.x) for x in con],}")

            # TODO: Fix issue regarding constraints not being applied. Might have to do with same constraint being passed for different flows.
            # No new objects are created (same id)
            self.set_constraints(constraints)
            self.solve_terminals()

            # Purely aestetic. Wrap into grap function or smth
            for flow in self.flows:
                print (" ")
                self.graph.reset_node_states()
                for node in flow.path:
                    node.state = flow.state.lower()
                self.graph.display_graph()

            # Pick first one, fix later
            collissions = self.find_first_conflict()

            # Collissions return none, one flow didnt have a path
            if not collissions:
                print ("No path")
                continue


            # Solution is valid if no collissions
            # TODO: Rework how i end the search, this is pure jank
            if collissions == True:
                print ("\nSolution Found")
                self.graph.reset_node_states()
                for flow in self.flows:
                    for node in flow.path:
                        node.state = flow.state.lower()
                self.graph.display_graph()
                return self.flows

            # DEBUG
            for colli in collissions:
                print (f"{colli[0].y, colli[0].x}: {*[x.state for x in colli[1]],}")

            for collission in collissions:

                node, flows = collission
                for flow in flows:

                    new_constraints = {state: set(nodes) for state, nodes in constraints.items()}
                    new_constraints[flow.state].add(node)

                    # TODO: Make not stupid
                    #new_constraints[flow.state] = set(new_constraints[flow.state])

                    new_cbs_node = cbs_node(new_constraints)
                    node_cost = self.amount_constraints(new_constraints)

                    heapq.heappush(open, (node_cost, next(counter), new_cbs_node))

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
    5,
    [
        "D", ".", ".", ".", ".",
        "B", ".", ".", "B", ".",
        "*", ".", ".", ".", ".",
        "C", ".", "A", ".", "D",
        "A", ".", ".", ".", "C",
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
g = graph(medium)

# Solver
cbs = CBS_solver(g)

cbs.solve_puzzle()

# Saving all terminals, i can easily change their state to * for other terminal colors such that they appear as not in play
# Either: Make a copy of the board so i can change states and maka truly local board
# Or: Check the state of squares i investigate and whether or not they are valid for my starting state

# works. if i want to ill optimize to not check already found neighbors, but, i
# dont think it will affect it in the long run
# As of now, it prefers routes on the outside, i believe this is due to the tie breaker
