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
16,1,2,0,4,2,7,1,2,14
"""

#data = test_data.splitlines()
#data = test_data
#data = test_data.split("\n\n")


def solve(data):
    crabs = list(map(int, data.split(",")))
    m = mean(crabs)
    min_dist = -1
    x = crabs[0]
    for c in range(len(crabs)):
        dist = sum([abs(crab - c) for crab in crabs])
        if min_dist == -1:
            x = c
            min_dist = dist
        elif dist < min_dist:
            min_dist = dist
            x = c
    return min_dist



def solve2(data):
    crabs = list(map(int, data.split(",")))
    m = mean(crabs)
    min_dist = -1
    x = crabs[0]
    for c in range(len(crabs)):
        dist = sum([abs(crab - c)*(abs(crab-c)+1)/2 for crab in crabs])
        if min_dist == -1:
            x = c
            min_dist = dist
        elif dist < min_dist:
            min_dist = dist
            x = c
    return min_dist

def median(l):
    if len(l) % 2 == 0:
        return (l[len(l)//2] + l[len(l)//2-1])/2
    else:
        return l[len(l)//2]

def mean(l):
    return sum(l)/len(l)


crabs = sorted(list(map(int, data.split(","))))
m = median(crabs)
me = int(mean(crabs))
print(sum(map(lambda x: abs(x-m), crabs)))
print(sum(map(lambda x: abs(x-me)*(abs(x-me)+1)/2, crabs)))

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
