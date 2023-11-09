from argparse import Action


class Node:
    # Initialize
    def __init__(self, state, parent, action, level, f_value):
        self.state = state
        self.parent = parent
        self.action = action        # List of actions to get to this node
        self.level = level
        self.f_value = f_value

    def __lt__(self, other):
        return self.f_value < other.f_value
    
    # Printing a node prints its action list, f_value, level, and state
    def __str__(self):
        state = ""
        for layer in self.state:
            for line in layer:
                for element in line:
                    state += str(element)
                    state += ' '
                state += '\n'
            state += '\n'
        
        action_list = ' '.join(self.action)
        f_value = str(self.f_value)
        level = str(self.level)
        return "ACTION LIST: " + action_list + '\nF_VALUE: ' + f_value + "\nLEVEL: " + level + "\nSTATE\n" + state
  
