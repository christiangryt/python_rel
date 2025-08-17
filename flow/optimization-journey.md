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

## Heap Optimization
Order of solution quality (amount-constraints, Board Fill, amount-collissions).     

From preliminary tests if amount-constraints not first solution time explodes:  

    Suggests node sellection has no idea where to go.   
    Meaning those boards i can solve are solved because the solution requires few constraints   

    and NOT because it knows where to look (possible aspect of the problem)  

Thoughts:

    Board Fill, Amount Collissions, Amount Constraints

    Problems:

        Amount Collissions logically harder to implement. Should take that battel some time     

## Astar path finding

Thought:    

    Make A* prioritize paths more likely to be correct,     

        Ideally,    
            No pocket squares,  
            No unreachable Terminals,   

        Reallistically,     
            A* prioritize paths along edge of board     
