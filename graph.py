# Project Team Members: Yongwen Lei and Thu Vu

from node import Node
import queue
import copy


class AStar:
    def __init__(self, init_state, goal_state, actions):
        self.init_state = init_state
        self.goal_state = goal_state
        self.curr_node = None  # The current node the algorithm is looking at
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

    # Make into all tuples
    def make_tuple(self, state):
        return tuple(tuple(tuple(inner_list) for inner_list in state[i]) for i in range(3))

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
        new_state = copy.deepcopy(curr_state)
        # Perform action
        if action == 'E' and y != 2:
            new_state[level][x][y], new_state[level][x][y + 1] = new_state[level][x][y + 1], new_state[level][x][y]

        elif action == 'W' and y != 0:
            new_state[level][x][y], new_state[level][x][y - 1] = new_state[level][x][y - 1], new_state[level][x][y]

        elif action == 'N' and x != 0:
            new_state[level][x][y], new_state[level][x - 1][y] = new_state[level][x - 1][y], new_state[level][x][y]

        elif action == 'S' and x != 2:
            new_state[level][x][y], new_state[level][x + 1][y] = new_state[level][x + 1][y], new_state[level][x][y]

        elif action == 'U' and level != 0:
            new_state[level][x][y], new_state[level - 1][x][y] = new_state[level - 1][x][y], new_state[level][x][y]

        elif action == 'D' and level != 2:
            new_state[level][x][y], new_state[level + 1][x][y] = new_state[level + 1][x][y], new_state[level][x][y]

        return new_state

    # Expand a node
    def expand(self, curr_node):
        s = curr_node.state
        # Apply each action to current node and return its child node
        for action in self.actions:
            new_parent = curr_node
            new_s = self.result(s, action)
            new_level = new_parent.level + 1
            new_f_value = self.get_h_value(new_s) + new_level
            new_action = copy.deepcopy(new_parent.action)
            new_action.append(action)
            yield Node(new_s, new_parent, new_action, new_level, new_f_value)

    # Perform A* search
    def search(self):
        # Initialize root node
        self.curr_node = Node(self.init_state, None, [], 0, 0)
        self.curr_node.parent = self.curr_node
        init_f = self.get_h_value(self.curr_node.state)
        self.curr_node.f_value = init_f

        self.reached[self.make_tuple(self.curr_node.state)] = self.curr_node
        self.frontier.put(self.curr_node)

        # Expand highest priority node while frontier is not empty
        while not self.frontier.empty():
            curr_node = self.frontier.get()
            self.curr_node = curr_node

            # If found, return the goal node
            if curr_node.state == self.goal_state:
                return curr_node

            # Expand current node
            for child in self.expand(curr_node):

                tuple_state = self.make_tuple(child.state)
                self.curr_node = child

                # Add child node to reached table and frontier
                if tuple_state not in self.reached or child.f_value < self.reached[tuple_state].f_value:
                    self.reached[tuple_state] = child
                    self.frontier.put(child)
        return -1
