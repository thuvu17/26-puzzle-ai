# Project Team Members: Yongwen Lei and Thu Vu

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

from graph import AStar


def main():
    # VARIABLES
    input_file = "InputFileName.txt"
    output_file = "OutputFileName.txt"
    input_data = ""
    output_data = ""
    init_state = [([[], [], []]) for i in range(3)]
    goal_state = [([[], [], []]) for i in range(3)]

    # READ INPUT
    with open(input_file) as f:
        i = 0
        # Read only the first 23 lines
        for j in range(23):
            line = f.readline()
            # Remove the newline character at the end if there is one
            if j == 22:
                line = line.strip()
            input_data += line
            output_data += line
            line = line.strip()
            # Format the initial state and goal state
            read_states(i, line, init_state, goal_state)
            i += 1
        f.close()

    # Create A* search algorithm and Perform A* search
    actions = ['E', 'W', 'S', 'N', 'U', 'D']
    a_star = AStar(init_state, goal_state, actions)
    found = a_star.search()

    # Write results to output file
    write_output_file(output_file, output_data, a_star)
    exit()


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
    elif 12 <= line_num < 23 and line_num not in (15, 19):
        if line_num < 15:
            goal_state[0][line_num % 12] = list(map(int, input_line.split()))
        elif line_num < 19:
            goal_state[1][line_num % 16] = list(map(int, input_line.split()))
        else:
            goal_state[2][line_num % 20] = list(map(int, input_line.split()))


# Get list of f(n) values along the optimal path by back-tracing
def get_f_value_list(final_node, init_state):
    f_value_list = [final_node.f_value]
    parent_node = final_node.parent

    while parent_node.state != init_state:
        f_value_list.insert(0, parent_node.f_value)
        parent_node = parent_node.parent

    f_value_list.insert(0, parent_node.f_value)

    return f_value_list


# Write results from A* search to output file
def write_output_file(output_file, output_data, result_graph):
    outf = open(output_file, "w")

    depth_shallowest_goal = result_graph.curr_node.level
    total_num_nodes = len(result_graph.reached)
    actions = result_graph.curr_node.action
    f_value_list = get_f_value_list(result_graph.curr_node, result_graph.init_state)

    output_data += "\n\n"  # line 24 is blank
    output_data += str(depth_shallowest_goal) + '\n'  # line 25 is depth of shallowest goal
    output_data += str(total_num_nodes) + '\n'  # line 26 is total number of nodes
    output_data += ' '.join(actions) + '\n'  # line 27 is sequence of actions
    output_data += ' '.join([str(n) for n in f_value_list])

    outf.write(output_data)
    outf.close()


if __name__ == "__main__":
    main()
