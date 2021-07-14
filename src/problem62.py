"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
from functools import reduce
from itertools import permutations

from src.utils import timer


@timer
def problem62():
    i = 21
    while True:
        i += 1
        cube = i**3
        cube_str = str(cube)
        cubic_perms_list = set()
        for perm in permutations(cube_str):
            perm_int = int(''.join(perm))
            if perm_int < cube:
                continue
            if int(round(perm_int ** (1 / 3))) ** 3 == perm_int:
                cubic_perms_list.add(perm_int)
        if len(cubic_perms_list) >= 3:
            print(cube, cubic_perms_list)
            break
    return i ** 3


@timer
def problem62_2():
    i = 21
    cubes_dict = dict()
    while True:
        i += 1
        cube = i**3
        key = tuple(sorted(str(cube)))
        if cubes_dict.get(key) is None:
            cubes_dict[key] = [cube]
        else:
            cubes_dict[key].append(cube)
            if len(cubes_dict[key]) == 5:
                print(cubes_dict[key])
                break

    return cubes_dict[key][0]


if __name__ == "__main__":
    print(problem62_2())

