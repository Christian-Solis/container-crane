
# Represent the state of the search
class Problem:

    # Constructor
    def __init__(self, action, path_cost, state, queue, goal):
        self.action = action
        self.path_cost = path_cost
        self.state = state
        self.queue = queue
        self.goal = goal

    # Method that generates all the posible actions
    # Returns tuples (actions)
    def possibles(self, visited, height_lim):
        

    # Method that calculates the cost of the action
    def cost_action(action):
