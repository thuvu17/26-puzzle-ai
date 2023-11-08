from node import Node
import queue

State_Index = {}

class AStar:
    def __init__(self, init_state, goal_state, actions):
        self.init_state = init_state
        self.goal_state = goal_state
        self.actions = actions
        self.frontier = queue.PriorityQueue()
        self.reached = {}

    # Find h value of child
    def get_h_value(self, curr_state):
        # Find sum of Manhattan distance
        h_value = 0
        for line in range(3):
            for x in range(3):
                for y in range(3):
                    curr_coords = (line, x, y)
                    curr_element = curr_state[line][x][y]
                    if curr_element != 0:
                        h_value += self.get_Manhattan_distance(curr_element, curr_coords)
        return h_value


    # Find Manhattan distance for one element
    def get_Manhattan_distance(self, target, curr_coords):
        goal_coord = self.get_coords(target, self.goal_state)
        return sum(abs(curr_coords[i] - goal_coord[i]) for i in range(3))


    # Find level, x, y of a target number
    def get_coords(self, target, state):
        for level in range(3):
            for x in range(3):
                for y in range(3):
                    if state[level][x][y] == target:
                        return (level, x, y)
    
          
    # Return result of performing an action on current state
    def result(self, curr_state, action):
        blank_curr_position = self.get_coords(0, curr_state)
        level = blank_curr_position[0]
        x = blank_curr_position[1]
        y = blank_curr_position[2]
        new_state = curr_state.copy()
        # Perform action
        if action == 'E' and y != 2:
            new_state[level][x][y], new_state[level][x][y + 1] = new_state[level][x][y + 1], new_state[level][x][y]
        elif action == 'W' and y != 0:
            new_state[level][x][y], new_state[level][x][y - 1] = new_state[level][x][y - 1], new_state[level][x][y]
        elif action == 'S' and x != 2:
            new_state[level][x][y], new_state[level][x + 1][y] = new_state[level][x + 1][y], new_state[level][x][y]
        elif action == 'N' and x != 0:
            new_state[level][x][y], new_state[level][x - 1][y] = new_state[level][x - 1][y], new_state[level][x][y]
        elif action == 'U' and level != 0:
            new_state[level][x][y], new_state[level - 1][x][y] = new_state[level - 1][x][y], new_state[level][x][y]
        elif action == 'D' and level != 2:
            new_state[level][x][y], new_state[level + 1][x][y] = new_state[level + 1][x][y], new_state[level][x][y]
        return new_state


    def expand(self, curr_node):
        s = curr_node.state
        children_list = []
        for action in self.actions:
            new_s = self.result(s, action)
            new_level = curr_node.level + 1
            new_f_value = self.get_h_value(new_s) + new_level
            child = Node(new_s, curr_node, action, new_level, new_f_value)
            children_list.append(child)
        for child in children_list:
            print('1 ')
        return children_list


    def search(self):
        init_node = Node(self.init_state, None, None, 0, 0)
        init_f = self.get_h_value(init_node.state)
        init_node.f_value = init_f
        print(init_node.f_value)
        State_Index[0] = init_node.state
        self.reached[0] = init_node
        self.frontier.put(init_node)
        print(self.frontier.empty())
        while not self.frontier.empty():
            curr_node = self.frontier.get()
            if curr_node.state == self.goal_state:
                print("found")
                return curr_node
            children = self.expand(curr_node)
            for child in children:
                State_Index[len(State_Index)] = child.state
                if child.state in State_Index.values():
                    for key in State_Index.keys():
                        if State_Index[key] == child.state:
                            child_state_index = key
                if child_state_index not in self.reached.keys() or child.f_value < self.reached[child.state].f_value:
                    self.reached[child_state_index] = child
                    self.frontier.put(child)
        return

