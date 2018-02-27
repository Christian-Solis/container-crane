
# Represent the node of the search
class Search_Node:

    # Constructor
    def __init__(self, parent, action, state, cost):
        self.parent = parent
        self.action = action
        #self.path_cost = path_cost
        self.state = state
        self.cost = cost

    # Child Node that returns new search node
    def child_node(self, new_action, height_lim, new_state, heuristic):
        # action is now the new action
        action = new_action
        # child converts to parent
        parent = self
        # cost is the cost of the parent plus cost of the action
        cost = parent.cost + Path_cost

        
