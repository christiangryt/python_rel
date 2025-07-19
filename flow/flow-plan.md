# Programs

- Program to make new levels
- Solver
- (option) Time race script

# Plan

## Make boards
Draw "strings/threads" on a matrix with no overlaps. - easier said than done  

Pick a random point, go any direction not backwards, random chance to stop at any time - need to check wether proposed change would make board unsolvable or not  

Try to use some sort of noise function (need to learn this with internet). lay noise function and translate to nxm matrix and find threads/strings (or atleast connect regions of similar noise) - could to be difficult, but good source of randomness   

Research if algorithms exist for this type of problem (try to find what kind of problem i am trying to solve here   
> Perhaps a modified shortest path algorithm that removes a cells path after each choice. each cell would have a path to each bordering cell (possible to simplify problem from this) and then pick shortest possible path (of those that are still available) and then remove said path. 
> Picking a start and an end point, either chose to points that have a path to each other or "try" (somehow) and end at the furthest point

## Solve boards

To solve these boards, we arrive at the Multi Agent Pathfinding problem, it is NP-Hard.     

Have not yet found a description of how to go forth finding these paths. There are 2 things i took away from reading the wiki. 1. backtracking seems to be a good base to start from, and 2. i am not yet sure how to guide the pathfinding. many people mention A\*, but this requires a wheightes graph and some semblence of types of connections, while in flow all edges are the same. One could weigh it on trying to go on the perimeter, but even still, that seems to simple, but maybe backtracking solves this.     

I therefore want to simply try my hand at making a backtracking algorithm using node objects with defined neighbors and working from there.     

### Convert to Maximum Flow problem

Given n flow threads (green, blue, red, etc) pick a node as a starting node.    

Find possible squares it is possible to reach (not going backwords as this is implicit due to flow being bidirectional **except starting nodes, these will only have flow out**) and also skipping previously inspected squares, but this seems obvious  

Doing this for the entire square leads to a flow diagram where it is possible to make a super source and sink and run normal maximum flow algorithms. *(problem is to make sure only each color can complete each color)*     

*Also implicit that each vertex (neighbouring squares) has capacity 1 and squares also have capacity 1, threads cannot share a square and only one thread can end in a square*    

> Problem: Reduction from nodes with capacity to normal maximum flow. As there are plenty of cycles present, this might prove difficult   
> > https://stackoverflow.com/questions/8751327/edmonds-karp-algorithm-for-a-graph-which-has-nodes-with-flow-capacities

*More efficient way: Have a standard fully connected square (all vertices are bi-directional), if the node is a source node, remove all in vertices and if it is a sink node remove alll out vertices. (This works with node capacity constraints as well)*  

> Unsure whether the cycles breaks this, but alas

#### Efficiency

This does not clearly solve the issue, as finding these augmenting paths from the flow network would in any non trivial board result in plenty of clearly incorrect paths     

Potentially no point in using maximum flow, as the difficult question does not lie in how much a path can carry, but rather what paths there are, and the existance of other paths simultaniously in the graph   

### BFS
Initial thoughts: BFS where every choice, checks if other paths become unsolvable or blocked in some way.   
> pick a start node for each color, go a direction (random or towards end point), check if other colors are able to be completed. 
> > Should start in each end, and work inwards

Essentially a backtracking, need to find optimizations, but pruning branches seems difficult as another net making a mistake could make a correct branch be pruned.   

For each starting node/terminal pick an available non breaking square, check if the move is valid, else pick another, none available go back to last square. Then go another starting node.     

### "River routing algorithm"

Algorithm that solves the problem how to most efficiently wire wireboards, smack in the middle. Might need to adjust for the fact that flow has terminals in the middle of the board and not only on the edges, but this looks promising  

#### To specific

The rive routing algorithm assumes terminals around the channel, but in flow these terminals are everywhere but around.
