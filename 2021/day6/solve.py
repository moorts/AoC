import subprocess

import numpy as np
from functools import *
from parse import parse

def ints_it(it):
    while it:
        yield int(it.pop(0))

def ints(it):
    return list(ints_it(it))

""" Interpreter code (just in case)
    x = 0
    depth = 0
    aim = 0
    for inst in data:
        opc, arg = inst.split(" ")
        if opc == "forward":
            x += int(arg)
            depth += aim * int(arg)
        elif opc == "down":
            aim += int(arg)
        elif opc == "up":
            aim -= int(arg)
"""

with open('./input') as f:
    data = f.read() # raw data
    #data = f.read().splitlines() # lines
    #data = f.read().split("\n\n") # Paragraphs

test_data = """\
3,4,3,1,2
"""

#data = test_data.splitlines()
#data = test_data
#data = test_data.split("\n\n")


def solve(data):
    fish = list(map(int, data.replace("\n", "").split(",")))
    for i in range(80):
        new = 0
        for i in range(len(fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
    return len(fish)
            

from collections import Counter

def solve2(data):
    fish = list(map(int, data.replace("\n", "").split(",")))
    counts = Counter(fish)
    for i in range(256):
        six = 0
        eight = 0

        for j in range(9):
            if counts[j] == 0:
                continue

            if j == 0:
                six += counts[j]
                eight += counts[j]
            else:
                counts[j-1] += counts[j]
            counts[j] = 0
        counts[6] += six
        counts[8] += eight
    return sum(counts.values())





from time import perf_counter

#first_result = solve(data)
before = perf_counter()
second_result = solve2(data)
after = perf_counter()

print(f"Method One: {after-before}")
#print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")

import numpy as np

before = perf_counter()
fish = list(map(int, data.replace("\n", "").split(",")))

s = np.zeros((9), dtype=np.int64)
for i in range(9):
    s[i] = fish.count(i)

v = s

r = np.matrix(
        [
            [0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0]
        ], dtype=np.int64)


v = v.dot(r**256)
after = perf_counter()
print(f"Method Two: {after-before}")
s = 0
print(sum(v.A[0]))
