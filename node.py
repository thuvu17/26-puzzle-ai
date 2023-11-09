from argparse import Action


class Node:
    # Initialize
    def __init__(self, state, parent, action, level, f_value):
        self.state = state
        self.parent = parent
        self.action = action
        self.level = level
        self.f_value = f_value

    def __lt__(self, other):
        return self.f_value < other.f_value
  
