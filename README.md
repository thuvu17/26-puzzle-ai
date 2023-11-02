<h1 align=center> 26 Puzzle Problem</h1>

## Project Description
Implement the A* search algorithm with graph search (no repeated states) 
for solving the 26-puzzle problem as described below. Use h(n)= Sum of Manhattan distances of 
the tiles from their goal positions as heuristic function. Your program will read in the initial and 
goal states from an input file and then generate an output file that contains the solution. 

## Details
- The game board consists of three 3 x 3 grids stacked together. There are 26 tiles, numbered 1 to 26, and a blank position
- Frontier sorted by f(n) = h(n) + g(n) with g(n) as the path cost
- Heuristic function h(n) = sum of Manhattan distances = |delta x| + |delta y| + |delta z|
- Actions allowed: East(E), West(W), South(S), North(S), Up(U), Down(D)

<p align="center">
  <img src="https://github.com/thuvu17/26-puzzle-ai/assets/112644941/d7712407-4ed4-484f-a868-ee444856824e">
</p>

### Input
- Includes 23 lines
  - lines 1-11: initial state
  - line 12 is blank
  - lines 13-23: goal state

### Output
- Includes 28 lines
  - lines 1-23: same as input, line 24 is blank
  - line 25: depth of shallowest goal (root node = 0)
  - line 26: total number of nodes N (including root)
  - line 27: solution as sequence of actions (E, W, N, S U, D) separated by blank spaces
  - line 28: f(n) values of the nodes along the solution path, separated by blank spaces
