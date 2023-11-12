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
    INPUT_FILE = "INPUT2.txt"
    INPUT_DATA = ""
    OUTPUT_DATA = ""
    init_state = [([[], [], []]) for i in range(3)]
    goal_state = [([[], [], []]) for i in range(3)]

    # READ INPUT
    with open(INPUT_FILE) as f:
        i = 0
        for j in range(23):
            line = f.readline()
            if j == 22:
                line = line.strip()
            INPUT_DATA += line
            OUTPUT_DATA += line
            line = line.strip()
            read_states(i, line, init_state, goal_state)
            i += 1
        f.close()

    print("INITIAL STATE:")
    print_matrix(init_state)

    # Perform A* search
    actions = ['E', 'W', 'S', 'N', 'U', 'D']
    a_star = AStar(init_state, goal_state, actions)
    found = a_star.search()

    print("---------------------\nRESULT")
    if found:
        print("FOUND!")
        print("Number of nodes:", len(a_star.reached))
    else:
        print("Solution not found!!!")
    print("FINAL STATE:")
    print_matrix(a_star.curr_node.state)
    print("Actions:", a_star.curr_node.action)

    write_output_file(OUTPUT_DATA, a_star)
    exit()


# Simple matrix printing function
def print_matrix(matrix):
    for layer in matrix:
        for line in layer:
            for element in line:
                print(element, end=' ')
            print()
        print()


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

        # Get list of f(n) values along the optimal path


def get_f_value_list(final_node, init_state):
    f_value_list = [final_node.f_value]
    parent_node = final_node.parent

    while (parent_node.state != init_state):
        f_value_list.insert(0, parent_node.f_value)
        parent_node = parent_node.parent

    f_value_list.insert(0, parent_node.f_value)

    return f_value_list


def write_output_file(OUTPUT_DATA, result_graph):
    outf = open("output.txt", "w")

    depth_shallowest_goal = result_graph.curr_node.level
    total_num_nodes = len(result_graph.reached)
    actions = result_graph.curr_node.action
    f_value_list = get_f_value_list(result_graph.curr_node, result_graph.init_state)

    OUTPUT_DATA += "\n\n"  # line 24 is blank
    OUTPUT_DATA += str(depth_shallowest_goal) + '\n'  # line 25 is depth of shallowest goal
    OUTPUT_DATA += str(total_num_nodes) + '\n'  # line 26 is total number of nodes
    OUTPUT_DATA += ' '.join(actions) + '\n'  # line 27 is sequence of actions
    OUTPUT_DATA += ' '.join([str(n) for n in f_value_list])

    outf.write(OUTPUT_DATA)
    outf.close()


if __name__ == "__main__":
    main()
