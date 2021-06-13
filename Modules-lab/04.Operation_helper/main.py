from mapper import *

num_1, operator,num_2 = input().split(' ')
num_1 = float(num_1)
num2 = float(num_2)

print(mapper[operator](num_1,num_2)if mapper.get(operator) else "Invalid Operator")
