from argparse import Action



class Node:
    # Initialize
    def __init__(self, state, parent, action, cost, f_value):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.f_value = f_value
  
 