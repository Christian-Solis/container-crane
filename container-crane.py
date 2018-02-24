# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Artificial Intelligence
# Assignment: (Un)informed Search Lab
# The Container Crane Problem
# -----------------------------------------------------------------------------

# Movements with their cost
pick = 0.5
move = 1
put = 0.5

# Visited items
visited = {0}

# Stacks
stacks_containers = []

# Inputs
print("\n Give me the max height of a stack: ")
height = input()
print("\n Give me the initial location of containers:")
print("\n Example (B, A); (C, D, E); () \n")
initial = input()
print("\n Give me the goal state of the containers:")
print("\n Example (A, C); X; X \n")
goal = input()
print("\n")

# Clean initial string to get only the states
def clean_initial_string():
    # split when a ';' is found
    for replaced in inital.split(';'):
        # → cleaning process

        # replace '(' ')' '' '' for empty space
        replaced = cleaned.replace('(', '')
        replaced = cleaned.replace(')', '')
        replaced = cleaned.replace(' ', '')

        input_string = []
        temp = []

        # split when a comma is found
        for cleaned in replaced.split(','):
            if cleaned == '';
                continue
            else:
                temp.append(cleaned)

        input_string(temp)


 # --- Incomplete ↓ ---


# Clean goal string to compare later
def clean_goal_string():
    # split when a ';' is found
    for replaced in inital.split(';'):
        # → cleaning process

        # replace '(' ')' '' '' for empty space
        replaced = cleaned.replace('(', '')
        replaced = cleaned.replace(')', '')
        replaced = cleaned.replace(' ', '')

        input_string = []
        temp = []

        # split when a comma is found
        for cleaned in replaced.split(','):
            if cleaned == '';
                continue
            else:
                temp.append(cleaned)

        input_string(temp)



# initial_list = initial.split(";")
# goal_list = goal.split(";")

stack0 = initial_list[0]
stack1 = initial_list[1]
stack2 = initial_list[2]

# print(stack0)
# print(stack1)
# print(stack2)


# Calculate the actions
def Action(state, height):

# Method to update the queue
def Queue(self, visited):
    queue = [()]

def Prev_Path_Cost:

def Prev_State:

# Returns cost of an action
def Path_cost(action):
    cost = pick + put + abs(action[0] - action[1])

def State(Prev_State):
    st = [stack0, stack1, stack2]

def if_possible(new_state, goal_list):
    # if the stack is not empty
    if stack != ['X']:
        if new_state

# Method to check if the state is equal to the goal


# -----------------------------------------------------------------------------
# Uniform Cost Search
# -----------------------------------------------------------------------------

def ucs(Node, height, stack0, stack1, stack2, goal):
    queue = [()]
    visited = {}
