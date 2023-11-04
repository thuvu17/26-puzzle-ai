# Code structure
## 1. main
- main only handles I/O, and calling initialization(), a_star_search()
    - initialization(): init goal + root node, graph object

## 2. graph
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

## 3. node
- Attributes
    - state: current matrix
    - parent: pointer to parent node
    - action: list of action to go from root to node
    - cost: level
    - f_value = g(n) + h(n)

## 4. queue
- Implement prioriy queue for frontier
    - Pop
    - Add + sort by f(n)

# Pseudocode
```
def a_start_search(root, goal)
    init_node = root
    frontier = [] prioriy queue
    reached = [] hash table
    frontier.add(init_node)
    reached.add(init_node)

    while frontier is not empty:
        curr_node = frontier.pop()
        if curr_node.state == goal_state:
            return curr_node
        children = expand(curr_node)
        for child in children:
            if child.state not in reached.key or child.path_cost < reached[child.state].path_cost:
                reached[child.state] = child
                frontier.add(frontier)
    return failure
```

