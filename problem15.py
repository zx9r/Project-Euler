"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

from math import factorial

""" 
    Permutations with repetition
    m! / (m1! * m2! * ... * mn!)
"""
m1 = 20  # moves to the right
m2 = 20  # moves down
m = m1 + m2
print(factorial(m) // (factorial(m1) * factorial(m2)))
