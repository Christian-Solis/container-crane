# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés & Eduardo Josué Contreras Álvarez
# A01063685
# A01064882
# Artificial Intelligence
# Assignment: (Un)informed Search Lab
# The Container Crane Problem
# -----------------------------------------------------------------------------

import sys
import heapq

# Movements with their cost
pick = 0.5
move = 1
put = 0.5

# Initial cost
initial_cost = 0

# Visited items
visited = {0}

# Stacks
stacks_containers = []

# -----------------------------------------------------------------------------
# Parsing and cleaning process
# -----------------------------------------------------------------------------

# Clean initial string to get only the states
def clean_initial_string(initial_input):
    input_without_spaces = initial_input.replace(' ', '')
    cont_stacks = list()
    # split when a ';' is found
    stacks = input_without_spaces.split(';')
    for st in stacks:
        st = st.replace('(', '')
        st = st.replace(')', '')
        if st == '':
            cont_stacks.append(list())
        else:
            containers = st.split(',')
            cont_stacks.append(containers)
    return cont_stacks

# Clean goal string to compare later
def clean_goal_string(goal_input):
    input_without_spaces = initial_input.replace(' ', '')
    cont_stacks = list()
    # split when a ';' is found
    stacks = input_without_spaces.split(';')
    for st in stacks:
        st = st.replace('(', '')
        st = st.replace(')', '')
        if st == '':
            cont_stacks.append(list())
        else:
            containers = st.split(',')
            cont_stacks.append(containers)
    return cont_stacks

# -----------------------------------------------------------------------------
# Comparison of state vs goal state
# -----------------------------------------------------------------------------

def comparison(initial_input, goal_input):
	for elem in goal_input:
        counter = 0
		if elem != ['X']:
			if initial_input[elem] == goal_input[elem]:
				counter += 1
	if counter == len(goal_input):
		return True
	return False

# -----------------------------------------------------------------------------
# # Uniform Cost Search
# -----------------------------------------------------------------------------

def ucs(max_height, initial_input, goal_input, initial_cost):
    # Queue and visited nodes
    queue = []
    visited = []

    # Acumulated cost
    acumulated_cost = Problem.cost_action()

    # Get the string parsed and cleaned into array
    current_state = clean_initial_string(initial_input)
    # Get the goal string parsed and cleaned into array
    goal_state = clean_goal_string(goal_input)

    # test ---
    # print(current_state)
    # print("\n")
    # print(goal_state)

    queue = [(acumulated_cost, current_state)]

    while queue:

	    acumulated_cost = heapq.heappop(queue)
        current_state = heapq.heappop(queue)

	 	if comparison(current_state, goal_state):


# -----------------------------------------------------------------------------
# Start
# -----------------------------------------------------------------------------

if __name__ == '__main__':

    # Inputs
    print("\n Give me the max height of a stack: ")
    height = int(input())
    print("\n Give me the initial location of containers:")
    print("\n Example (B, A); (C, D, E); () \n")
    initial_input = input()
    print("\n Give me the goal state of the containers:")
    print("\n Example (A, C); X; X \n")
    goal_input = input()
    print("\n")

    ucs(height, initial_input, goal_input, initial_cost)

# -----------------------------------------------------------------------------
# Actions
# -----------------------------------------------------------------------------
#
# # Calculate the actions
# def Action(state, height):
#
# # Method to update the queue
# def Queue(self, visited):
#     queue = [()]
#
# def Prev_Path_Cost:
#
# def Prev_State:
#
# def State(Prev_State):
#     st = [stack0, stack1, stack2]
#
# def if_possible(new_state, goal_list):
#     # if the stack is not empty
#     if stack != ['X']:
#         if new_state
#
# # Method to check if the state is equal to the goal
#
