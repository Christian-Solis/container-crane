
# Represent the state of the search
class Problem:

    # Constructor
    def __init__(self, action, path_cost, state, queue, goal):
        self.action = action
        self.path_cost = path_cost
        self.state = state
        self.queue = queue
        self.goal = goal

    
