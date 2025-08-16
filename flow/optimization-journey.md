# Optimize solver

## Board fill Heuristic
Inverse proportion of free nodes to used nodes in all paths -> Less path overlap and more of the board used.
When tested on true medium board (7x7):

    No Board Fill: Visited 1324 Iterations

    With Board Fill: 124 Iterations

Easy Board (5x5):

    No Board Fill: 46 Iterations

    With Board Fill: 14 Iterations

Great Success. Still cannot Tackle Hard map i made

### Problems

Seems order of heap stacking affects if puzzle becomes solved. The program is not fast enough, i need to optimze more
