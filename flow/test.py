import heapq
# TODO:chatGPT løsning enn så lenge
import itertools

def astar(start, end, graph):
    """
    astar with simple shortest path heuristic
    node class objects as start and stop
    and graph class object
    """

    graph.reset_astar_values()
    counter = itertools.count()

    open = []
    closed = []

    # add starting node to open heap
    heapq.heappush(open, (start.f, next(counter), start))

    while open:
        # litt janky, men trenger ikke pri
        q = heapq.heappop(open)[-1]

        for neigh in q.neighbors:
            print (f"looking at {neigh}")
            if neigh == end:
                # returner nodene denne er innom
                # loop gjennom parents
                print ("Found exit")
                open = []

                """
                gg = q
                while gg != start:
                    print (q.parent)
                    gg =  q.parent
                """
                print (q.parent.parent.parent.parent)

                break

            g = q.g + 1
            h = abs(neigh.x - end.x) + abs(neigh.y - end.y)
            f = neigh.g + neigh.h

            if f < neigh.f or neigh.f == 0:
                heapq.heappush(open, (neigh.f, next(counter), neigh))

                neigh.f = f
                neigh.h = h
                neigh.g = g

                neigh.parent = q
                q.successor.append(neigh)

class node():

    def __init__(self, y, x):

        self.y = y
        self.x = x

        self.f = 0 # Total cost
        self.g = 0 # Cost to node from start
        self.h = 0 # Heuristic cost estimate

        self.neighbors = []
        self.parent = None
        self.successor = []

    def __repr__(self):
        return f"Node at ({self.y},{self.x})"

    def find_neighbors(self, d):
        """
        Given dictionary of nodes that exist, adds neighbors
        """

        neighbors = []

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
                neighbors.append(res)

        return neighbors

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
        """

        # Make nodes if square is in play
        self.nodes = [
                node (
                    i // graph[0],
                    i % graph[0]
                )

                for i,n in enumerate(graph[1])
                if n != "*"
            ]

        # Dictionary on coord tuple
        self.node_locations = {
                (n.y, n.x) : n for n in self.nodes
            }

        for n in self.nodes:
            n.neighbors = n.find_neighbors(
                    self.node_locations
                )

    def reset_astar_values(self):
        """
        Reset attr. to none and 0
        Unsure if this is best practice, but seeing as im going to have to run a* one million times...
        """

        for n in self.nodes:
            n.f = 0
            n.g = 0
            n.h = 0

            n.parent = None
            n.successor = []

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
        ["A", ".", "A","*", "B", ".","*", "*", "B"],
]

test2 = [
    5,
    [
        ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".",
    ]
]

# Make graph object
g = graph(test2)

start = g.node_locations.get((1,1))
end = g.node_locations.get((4,4))

astar(start, end, g)

# works. if i want to ill optimize to not check already found neighbors, but, i dont think it will affect it in the long run
