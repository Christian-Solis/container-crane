# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Artificial Intelligence
# Assignment: (Un)informed Search Lab
# The Container Crane Problem
# -----------------------------------------------------------------------------

import sys

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
    # split when a ';' is found
    for initial_string_replaced in initial_input.split(';'):
        # → cleaning process
        # replace '(' ')' '' '' for empty space
        initial_string_replaced = initial_string_replaced.replace('(', '')
        initial_string_replaced = initial_string_replaced.replace(')', '')
        initial_string_replaced = initial_string_replaced.replace(' ', '')

        input_string = []
        temp = []

        # split when a comma is found
        for cleaned in initial_string_replaced.split(','):
            if cleaned == '':
                continue
            else:
                temp.append(cleaned)

        # fill the array
        input_string.append(temp)

    # test ---
    #print(input_string)

    # return the array
    return input_string

# Clean goal string to compare later
def clean_goal_string(goal_input):
    # split when a ';' is found
    for goal_string_replaced in goal_input.split(';'):
        # → cleaning process
        # replace '(' ')' '' '' for empty space
        goal_string_replaced = goal_string_replaced.replace('(', '')
        goal_string_replaced = goal_string_replaced.replace(')', '')
        goal_string_replaced = goal_string_replaced.replace(' ', '')

        goal_string = []
        temp2 = []

        # split when a comma is found
        for cleaning in goal_string_replaced.split(','):
            if cleaning == '':
                continue
            else:
                temp2.append(cleaning)

        # fill the array
        goal_string.append(temp2)

    # test ---
    #print(goal_string)

    # return the array
    return goal_string


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
# # Returns cost of an action
# def Path_cost(action):
#     cost = pick + put + abs(action[0] - action[1])
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

# -----------------------------------------------------------------------------
# # Uniform Cost Search
# -----------------------------------------------------------------------------

def ucs(max_height, initial_input, goal_input, initial_cost):
    # Queue and visited nodes
    queue = []
    visited = []

	# Get the string parsed and cleaned into array
	current_state = clean_initial_string(initial_input)
    # Get the goal string parsed and cleaned into array
	goal_state = clean_goal_string(goal_input)

    # test ---
    # print(current_state)
    # print("\n")
    # print(goal_state)

    que
