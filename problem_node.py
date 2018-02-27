
# Represent the state of the search
class Problem:

    # Constructor
    def __init__(self, action, path_cost, state, queue, goal):
        self.action = action
        self.path_cost = path_cost
        self.state = state
        self.queue = queue
        self.goal = goal


    # if self.state == self.goal

    # Method that generates all the posible actions
    # Returns tuples (actions)
    def possibles(self, visited, height_lim, state):
        #if stack[0] + 1 <= height_lim:
            #if  

    # Method that calculates the cost of the action
    def cost_action(action):
        cost = pick + put + abs(action[0] - action[1])
        return cost
