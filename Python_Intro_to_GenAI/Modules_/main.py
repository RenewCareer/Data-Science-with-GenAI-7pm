# Import    a module with alias

import calculations as calc
result = calc.add(20, 3)
print(result)

import statistics as stats
data = [1, 2, 3, 4, 5]

mean = stats.mean(data)
print("Mean:", mean)

# Import specific functions from a module with alias

from calculations import multiply as product

result = product(4, 5)
print(result)

from calculations import *

# # Importing specific functions from a module
# from calculations import add, subtract

# print(add(8,9))



# import calculations

# result = calculations.add(5, 3)
# print(result)