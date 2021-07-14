"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import math
from itertools import combinations

from src.utils import timer, is_prime, is_prime_miller


def sieve(n):
    l = [0 if i % 2 == 0 and i != 2 else 1 for i in range(n)]
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if l[i] == 1 and is_prime(i):
            for j in range(i * 2, n, i):
                l[j] = 0
    return l


@timer
def problem60():
    primes = [i for i in range(3, 1000, 2) if i != 5 and is_prime(i)]
    dict_pairs = {p: {} for p in primes}
    #primes_list = {i: 1 for i in range(37, 100_000_000, 2) if is_prime(i)}
    primes_list = sieve(1000000)
    print(primes)
    min_sum = 0
    for primes5 in combinations(primes, 4):
        valid = True
        for primes2 in combinations(primes5, 2):
            prime_pair1 = dict_pairs[primes2[0]].get(primes2[1])
            if prime_pair1 is None:
                concat1 = int(f"{primes2[0]}{primes2[1]}")
                concat2 = int(f"{primes2[1]}{primes2[0]}")
                dict_pairs[primes2[0]][primes2[1]] = primes_list[concat1]
                dict_pairs[primes2[1]][primes2[0]] = primes_list[concat2]
                prime_pair1 = dict_pairs[primes2[0]][primes2[1]]
            prime_pair2 = dict_pairs[primes2[1]][primes2[0]]
            if not prime_pair1 or not prime_pair2:
                valid = False
                break
        if valid:
            primes_sum = sum(primes5)
            print(primes5, primes_sum)
            if min_sum == 0 or primes_sum < min_sum:
                min_sum = primes_sum
    return min_sum


def concat_int(i1, i2):
    return int(f"{i1}{i2}")


def calculate_concat_primes(primes, index):
    result = {}
    for i in range(index + 1, len(primes)):
        if is_prime_miller(concat_int(primes[index], primes[i])) and \
                is_prime_miller(concat_int(primes[i], primes[index])):
            result[primes[i]] = 1
    return result


@timer
def problem60_2():
    primes = [i for i in range(3, 10000, 2) if i != 5 and is_prime(i)]
    prime_pairs = [0] * len(primes)
    print(primes)
    min_sum = 50000 * 5
    for a in range(len(primes)):
        if primes[a] * 5 > min_sum:
            break
        if prime_pairs[a] == 0:
            prime_pairs[a] = calculate_concat_primes(primes, a)
        for b in range(a + 1, len(primes)):
            if primes[a] + primes[b] * 4 > min_sum:
                break
            if prime_pairs[b] == 0:
                prime_pairs[b] = calculate_concat_primes(primes, b)
            if not prime_pairs[a].get(primes[b]):
                continue
            for c in range(b + 1, len(primes)):
                if primes[a] + primes[b] + primes[c] * 3 > min_sum:
                    break
                if prime_pairs[c] == 0:
                    prime_pairs[c] = calculate_concat_primes(primes, c)
                if not prime_pairs[a].get(primes[c])\
                        or not prime_pairs[b].get(primes[c]):
                    continue
                for d in range(c + 1, len(primes)):
                    if primes[a] + primes[b] + primes[c] + primes[d] * 2 > min_sum:
                        break
                    if prime_pairs[d] == 0:
                        prime_pairs[d] = calculate_concat_primes(primes, d)
                    if not prime_pairs[a].get(primes[d]) \
                            or not prime_pairs[b].get(primes[d]) \
                            or not prime_pairs[c].get(primes[d]):
                        continue
                    for e in range(d + 1, len(primes)):
                        if primes[a] + primes[b] + primes[c] + primes[d] + primes[e] > min_sum:
                            break
                        if prime_pairs[e] == 0:
                            prime_pairs[e] = calculate_concat_primes(primes, e)
                        if not prime_pairs[a].get(primes[e]) \
                                or not prime_pairs[b].get(primes[e]) \
                                or not prime_pairs[c].get(primes[e]) \
                                or not prime_pairs[d].get(primes[e]):
                            continue

                        primes_sum = primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
                        print(f"({primes[a]}, {primes[b]}, {primes[c]}, {primes[d]}, {primes[e]}) {primes_sum}")
                        if min_sum == 0 or primes_sum < min_sum:
                            min_sum = primes_sum
    return min_sum


if __name__ == "__main__":
    print(problem60_2())
