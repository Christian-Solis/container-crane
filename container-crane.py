# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Artificial Intelligence
# Assignment: (Un)informed Search Lab
# The Container Crane Problem
# -----------------------------------------------------------------------------

pick = 0.5
move = 1
put = 0.5

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

print(stack0)
print(stack1)
print(stack2)
