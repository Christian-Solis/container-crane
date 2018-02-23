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

# Queue
queue = [()]

# Visited items
visited = {0}

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


initial_list = initial.split(";")
goal_list = goal.split(";")

stack0 = initial_list[0]
stack1 = initial_list[1]
stack2 = initial_list[2]

# print(stack0)
# print(stack1)
# print(stack2)

class Node:
    def __init__(Parent, Action, Path_Cost, State):

def Action():

def Prev_Path_Cost:

def Prev_State:


def Path_cost(Prev_Path_Cost):
    ptc = Prev_Path_Cost + pick + move + put

def State(Prev_State):
    st = [stack0, stack1, stack2]

# -----------------------------------------------------------------------------
# Uniform Cost Search
# -----------------------------------------------------------------------------

def ucs(Node, height, stack0, stack1, stack2, goal):
    queue = [()]
    visited = {}
