"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
n = 600851475143
largest_factor = 3
while n > 1:
    if n % largest_factor == 0:
        n = n / largest_factor
    else:
        largest_factor += 2

print(largest_factor)
