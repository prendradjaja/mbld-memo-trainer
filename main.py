from __future__ import print_function
from string import ascii_uppercase
import random
import sys


# TODO
# - Use arg parser
# - Make last cube swap optional


if len(sys.argv) > 1:
    NUM_CUBES = int(sys.argv[1])
else:
    NUM_CUBES = 9

ALL_LETTERS = ascii_uppercase[:-2]
EDGE_LETTERS = list(set(ALL_LETTERS) - set('KU'))
CORNER_LETTERS = list(set(ALL_LETTERS) - set('AER'))

def random_even_int(minval, maxval):
    assert minval % 2 == 0 and maxval % 2 == 0
    spread = maxval - minval
    return minval + random.randint(0, spread // 2) * 2

def random_cube(reverse_order=False):
    parity = random.choice([True, False])
    num_edges = random_even_int(10, 12)
    num_corners = random_even_int(6, 8)
    num_flips = max(random.randint(-1, 2), 0)
    num_twists = max(random.randint(-1, 2), 0)
    if parity:
        num_edges += 1
        num_corners += 1
    edges = random_memo(num_edges, EDGE_LETTERS)
    corners = random_memo(num_corners, CORNER_LETTERS)
    flips = random_memo(num_flips, EDGE_LETTERS)
    twists = random_memo(num_twists, CORNER_LETTERS)
    fliptwist_delimiter = '  ~  '
    if not reverse_order:
        return (
            edges   + fliptwist_delimiter + flips  + '\n' +
            corners + fliptwist_delimiter + twists + '\n\n'
        )
    else:
        return (
            corners + fliptwist_delimiter + twists + '\n' +
            edges   + fliptwist_delimiter + flips  + '\n\n'
        )

def random_memo(length, letters):
    result = ''
    for i in range(length):
        result += random_letter(letters)
        j = i + 1
        if j % 2 == 0:
            result += ' '
        if j % 4 == 0:
            result += ' '
    return result.strip()

def random_letter(letters):
    random_letter.num_calls += 1
    result = random_letter.previous_result
    while result == random_letter.previous_result:
        result = random.choice(letters)
    random_letter.previous_result = result
    return result
random_letter.num_calls = 0

random_letter.previous_result = None

for i in range(NUM_CUBES - 1):
    print(str(i + 1) + '.')
    print(random_cube(), end='')
print(str(NUM_CUBES) + '.')
print(random_cube(True), end='')

print('Total number of letters:', random_letter.num_calls)
