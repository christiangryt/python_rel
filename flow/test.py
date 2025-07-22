def astar(start, end, graph):
    """
    astar with simple shortest path heuristic
    node class objects as start and stop
    and graph class object
    """

    open = []
    closed = []

class node():

    def __init__(self, y, x):

        self.y = y
        self.x = x

        self.neighbors = []
        self.parent = None
        self.successor = None

    def __repr__(self):
        return f"Node at ({self.y},{self.x})"

    def get_neighbors(self):

        if self.parent:
            self.neighbors.remove(self.parent)

        return self.neighbors

class graph():

    def __init__(self, graph):
        """
        Given nested list like, f.ex.
        Where . is an empty square and * is not in use
        (I think passing a tuple/list where [0] is the length of each row and [1] being the flattened data. Easier to work with, and i can later make something to convert this below to said flattened structure)

        [
            ["A", ".", "A"],
            ["*", "B", "."],
            ["*", "*", "B"],
        ]

        Make node objects with correct neighbors and  states
        """

        self.nodes = None

        for row in graph:
            for node in row:

                if node != "*":
                    None

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

# works, might be better to spell it more out
nodes = [node(i // test[0], i % test[0]) for i,n in enumerate(test[1]) if n != "*"]
#print ([n.x for n in nodes])
print (nodes)

# find neighbors of each node
# first make dict to search for neighbors easily
y = 1
x = 1

# use dicts with tuples as key, very nice
my_dict = {(n.y, n.x) : n for n in nodes}
print (my_dict.get((y,x), "bacon"))

# works. if i want to ill optimize to not check already found neighbors, but, i dont think it will affect it in the long run
def find_neighbors(n, d):

    neighbors = []

    search = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    print ("---")
    print (n)
    for s in search:

        new_y = n.y + s[1]
        new_x = n.x + s[0]
        print (f"{new_y} {new_x}")

        res = d.get((new_y, new_x))
        print (res)

        if res:
            neighbors.append(res)

    return neighbors

for n in nodes:
    n.neighbors = find_neighbors(n, my_dict)

# dab and swag
print (nodes[2].neighbors)
