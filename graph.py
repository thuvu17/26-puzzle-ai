from node import Node

class Graph:
    def __init__(self, node):
        self.node = node
        self.frontier = []
        self.actions = ['E', 'W', 'S', 'N', 'U', 'D']
        

    # Find f value of child
    def get_f_value(self, goal_state):
        # Find sum of Manhattan distance
        h_value = 0
        curr_state = self.state
        for line in range(3):
            for x in range(3):
                for y in range(3):
                    curr_coords = (line, x, y)
                    curr_element = curr_state[line][x][y]
                    h_value += self.get_Manhattan_distance(curr_element, curr_coords, goal_state)
        return h_value + self.node.cost + 1


    # Find Manhattan distance for one element
    def get_Manhattan_distance(self, target, curr_coords, goal_state):
        goal_coord = self.get_coords(target, goal_state)
        return sum(abs(curr_coords[i] - goal_coord[i]) for i in range(3))


    # Find level, x, y of a target number
    def get_coords(self, target, state):
        for level in range(3):
            for x in range(3):
                for y in range(3):
                    if state[level][x][y] == target:
                        return (level, x, y)
    
          
    # Return result of performing an action on current state
    def result(self, action):
        blank_curr_position = self.get_coords(0, self.node.state)
        level = blank_curr_position[0]
        x = blank_curr_position[1]
        y = blank_curr_position[2]
        state = self.node.state.copy()
        # Perform action
        if action == 'E' and y != 2:
            state[level][x][y], state[level][x][y + 1] = state[level][x][y + 1], state[level][x][y]
        elif action == 'W' and y != 0:
            state[level][x][y], state[level][x][y - 1] = state[level][x][y - 1], state[level][x][y]
        elif action == 'S' and x != 2:
            state[level][x][y], state[level][x + 1][y] = state[level][x + 1][y], state[level][x][y]
        elif action == 'N' and x != 0:
            state[level][x][y], state[level][x - 1][y] = state[level][x - 1][y], state[level][x][y]
        elif action == 'U' and level != 0:
            state[level][x][y], state[level - 1][x][y] = state[level - 1][x][y], state[level][x][y]
        elif action == 'D' and level != 2:
            state[level][x][y], state[level + 1][x][y] = state[level + 1][x][y], state[level][x][y]
        return state


    def expand(self, goal_node):
        s = self.node.state
        children_list = []
        for action in self.actions:
            new_s = self.result(s, action)
            new_cost = self.node.cost + 1
            new_f_value = self.get_f_value(goal_node)
            child = Node(new_s, self.node, action, new_cost, new_f_value)
            children_list.append(child)
        return children_list

        
        