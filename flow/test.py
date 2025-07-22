graph = [
    ["A",".","."],
    ["B",".","."],
    ["-","B","A"]
]

for x in graph:
    for y in x:
        print (y)

class flow():
    """
    Plan for self:
    Represent a color (A->A). Calls path finding, this should be abstracted to more easily change the heuristics

    (This pathfinding needs to be easily able to respect the restrictions given by the CBS. I do have to solve it several times, but alas)
    """

    None
