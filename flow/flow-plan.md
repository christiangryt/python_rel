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

### BFS
Initial thoughts: BFS where every choice, checks if other paths become unsolvable or blocked in some way.   
> pick a start node for each color, go a direction (random or towards end point), check if other colors are able to be completed. 
> > Should start in each end, and work inwards

This could work, but the 
