import heapq
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
