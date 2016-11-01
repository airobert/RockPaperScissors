
from pulp import *

prob = LpProblem("test1", LpMinimize)

# Variables
x1 = LpVariable("x1", 0, 1)
x2 = LpVariable("x2", 0, 1)
x3 = LpVariable("x3", 0, 1)
v = LpVariable("v", 0)

# Objective
prob += v

# Constraints
prob += v <= x2 - x3
prob += v <= -1 * x1 + x3
prob += v <= x1 - x2
prob += x1 + x2 + x3 == 1 


GLPK().solve(prob)

# Solution
for v in prob.variables():
	print (v.name, "=", v.varValue)

print ("objective=", value(prob.objective))  


# from pulp import *

# prob = LpProblem("test1", LpMinimize)

# # Variables
# x = LpVariable("x", 0, 4)
# y = LpVariable("y", -1, 1)
# z = LpVariable("z", 0)

# # Objective
# prob += x + 4*y + 9*z

# # Constraints
# prob += x+y <= 5
# prob += x+z >= 10
# prob += -y+z == 7

# GLPK().solve(prob)

# # Solution
# for v in prob.variables():
# 	print (v.name, "=", v.varValue)

# print ("objective=", value(prob.objective))  

