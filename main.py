#  __________ PROBLEM PROMPT ___________
# Implement A* search algorithm, no repeated states
# h(n) = sum of Manhattan distances = |delta x| + |delta y| + |delta z|

# INPUT (23 lines)
# lines 1-11: initial state (3 3 3), line 12 is blank, lines 13-23: goal state (3 3 3)

# OUTPUT (28 lines)
# lines 1-23: same as input, line 24 is blank, line 25: depth of shallowest goal (root node = 0)
# line 26: total number of nodes N (including root)
# line 27: solution as sequence of actions (E, W, N, S U, D) separated by blank spaces
# line 28: f(n) values of the nodes along the solution path, separated by blank spaces

from node import Node
from graph import AStar

def main():
    # VARIABLES
    INPUT_FILE = "input.txt"
    INPUT_DATA = ""
    init_state = [([[], [], []]) for i in range(3)]
    goal_state = [([[], [], []]) for i in range(3)]
    total_nodes = 1
    
    # READ INPUT
    with open(INPUT_FILE) as f:
        i = 0
        for line in f:
            INPUT_DATA += line
            line = line.strip()
            read_states(i, line, init_state, goal_state)
            i += 1
        f.close()
    
    # print(get_h_value(init_state, goal_state))
    solution = a_star_search(init_state, goal_state)
    # print(solution.action)
    

def a_star_search(init_state, goal_state):
    actions = ['E', 'W', 'S', 'N', 'U', 'D']
    searching_algo = AStar(init_state, goal_state, actions)
    solution = searching_algo.search()
    print(searching_algo.init_state)
    return solution
    

# # Find sum of Manhattan distance
# def get_h_value(init_state, goal_state):
#     h_value = 0
#     for line in range(3):
#         for x in range(3):
#             for y in range(3):
#                 curr_coords = (line, x, y)
#                 curr_element = init_state[line][x][y]
#                 if curr_element != 0:
#                     h_value += get_Manhattan_distance(curr_element, curr_coords, goal_state)
#     return h_value
#
#
# # Find Manhattan distance for one element
# def get_Manhattan_distance(target, curr_coords, goal_state):
#     goal_coord = get_coords(target, goal_state)
#     return sum(abs(curr_coords[i] - goal_coord[i]) for i in range(3))


# # Find level, x, y of a target number
# def get_coords(target, matrix):
#     for level in range(3):
#         for x in range(3):
#             for y in range(3):
#                 if matrix[level][x][y] == target:
#                     return (level, x, y)


# Simple matrix printing function
def print_matrix(matrix):
    for line in matrix:
        print(line)


# Read an input string into initial and goal states
def read_states(line_num, input_line, init_state, goal_state):
    # Reading initial state
    if line_num < 11 and line_num not in (3, 7):
        if line_num < 3:
            init_state[0][line_num] = list(map(int, input_line.split()))
        elif line_num < 7:
            init_state[1][line_num % 4] = list(map(int, input_line.split()))
        else:
            init_state[2][line_num % 8] = list(map(int, input_line.split()))
    # Reading goal state
    elif line_num >= 12 and line_num < 23 and line_num not in (15, 19):
        if line_num < 15:
            goal_state[0][line_num % 12] = list(map(int, input_line.split()))
        elif line_num < 19:
            goal_state[1][line_num % 16] = list(map(int, input_line.split()))
        else:
            goal_state[2][line_num % 20] = list(map(int, input_line.split()))            
    

if __name__ == "__main__":
    main()
