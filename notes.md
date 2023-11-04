# Code structure
## main
- main only handles I/O, and calling initialization(), a_star_search()
    - initialization(): init goal + root node, graph object

## graph
- Includes implementations of:
    - Manhattan distance
    - search(goal node, current node)
    - expand
    - result(state, action)

- Attributes
    - Frontier: a priority queue
    - Reached table: hash table (key: state, value: pointer to node)
    - Goal state: pointer to goal node
    - Initial state: pointer to root node

## node
- Attributes
    - state: current matrix
    - parent: pointer to parent node
    - action: list of action to go from root to node
    - cost: level
    - f_value = g(n) + h(n)

## queue
- Implement prioriy queue for frontier
    - Pop
    - Add + sort by f(n)

# Outline
1. main calls initialize(): create initial + goal state + graph
2. main calls a_start_search(graph)
3. 