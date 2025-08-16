import heapq
from collections import defaultdict
# TODO:chatGPT løsning enn så lenge
import itertools

from graph import *
from astar import *

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

        # DEBUG
        #print(f"{self.state} : {[(x.y, x.x, x.state) for x in self.constraints]}")

        # TODO: Add potential to easily change path finding
        self.path = astar(start, end, self.graph, self.constraints)

        #self.graph.add_neighbors()

class cbs_node():

    def __init__(self, constraints, paths):

        self.constraints = constraints
        self.paths = paths

class CBS_solver():
    """
    Note to self, this is the object that should make CBS_nodes and handle solving.
    Flow class keeps track of a single path, this keeps track of all tracks
    """

    def __init__(self, graph,drawer=None, with_curses=False):

        self.flows = []
        self.graph = graph

        # output to curses
        self.with_curses = with_curses

        # First make flow objects from all_terminals list
        for state, nodes in self.graph.terminals.items():
            self.flows.append(flow(self.graph, nodes, state))

    def board_fill(self, paths):

        used_nodes = set()
        for _, path in paths:
            for node in path:
                used_nodes.add(node)

        # + 1 to inhibit any divide by 0 error
        return  len(self.graph.usable_nodes) / (len(used_nodes) + 1 )

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

        paths = []

        for flow in self.flows:
            flow.solve_terminal()

            # Make sure no new objects are created from this
            paths.append((flow, flow.path))

        return paths

    # Should CBS have any visuals?
    def display_all_flows(self, with_curses=False):
        """
        with_curses:
            False   Print each board

            True    Return List of nested boards
        """

        None

    def find_first_conflict(self, paths):
        """
        Finds approximation to error with no prior error based on distance to terminals
        """

        # Flow and path index
        usage = defaultdict(list)

        # Might be ugly and stupid
        for flow, path in paths:

            path_length = len(path)
            if path_length == 0:
                return False

            for node_index, node in enumerate(path):
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

        # TODO: Expand logging
        iteration_count = 0

        # Flow + list of constraints
        constraints = defaultdict(set)

        constraint_cost = self.amount_constraints(constraints)
        counter = itertools.count()
        self.set_constraints(constraints)
        paths = self.solve_terminals()
        cost = self.board_fill(paths)

        root = cbs_node(constraints, paths)

        # Solutions to check
        open = []
        heapq.heappush(open, (constraint_cost, cost, next(counter), root))

        while open:

            print ("---")

            iteration_count += 1

            # Least constraints
            P = heapq.heappop(open)[-1]

            collissions = self.find_first_conflict(P.paths)

            # Collissions return False, one flow didnt have a path
            if not collissions:
                print ("No path")
                continue

            # Solution is valid if no collissions
            # TODO: Rework how i end the search, this is pure jank
            if collissions == True:
                print ("\nSolution Found")
                self.graph.reset_node_states()
                for flow, path in P.paths:
                    for node in path:
                        node.state = flow.state.lower()
                self.graph.display_graph()
                print (iteration_count)
                return self.flows

            # TODO: Prettier logging. All DEBUG must play nice with curses
            # DEBUG
            for colli in collissions:
                print (f"{colli[0].y, colli[0].x}: {*[x.state for x in colli[1]],}")

            # Make 2 nodes, reduce breadth or smth
            node, flows = collissions[0]
            for flow in flows:

                # TODO: ????? Why does this work
                node = collissions[0][0]

                #new_constraints = {state: set(nodes) for state, nodes in P.constraints.items()}
                new_constraints = defaultdict(set, {
                    state: set(nodes) for state, nodes in P.constraints.items()
                })
                new_constraints[flow.state].add(node)

                # DEBUG
                for state, con in new_constraints.items():
                    print (f"{state}: {*[(x.y,x.x) for x in con],}")

                self.set_constraints(new_constraints)
                new_paths = self.solve_terminals()
                new_cost = self.board_fill(new_paths)

                new_cbs_node = cbs_node(new_constraints, new_paths)
                node_cost = self.amount_constraints(new_constraints)

                # Purely aestetic. Wrap into grap function or smth
                for flow, path in P.paths:
                    print (" ")
                    self.graph.reset_node_states()
                    for node in path:
                        node.state = flow.state.lower()
                    self.graph.display_graph()

                heapq.heappush(open, (node_cost, new_cost, next(counter), new_cbs_node))
