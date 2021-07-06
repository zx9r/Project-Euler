from utils import is_prime


def cuadratic(a, b):
    def response(x):
        return abs(x**2 + a * x + b)
    return response


max_a = max_b = 0
max_primes = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        f = cuadratic(a, b)
        primes = 0
        x = 0
        while is_prime(f(x)):
            primes += 1
            x += 1
        if primes > max_primes:
            max_a = a
            max_b = b
            max_primes = primes
            print("a: {} b: {} primes: {}".format(max_a, max_b, max_primes))

print(max_a * max_b)
