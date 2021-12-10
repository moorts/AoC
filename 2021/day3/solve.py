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
    #data = f.read() # raw data
    data = f.read().splitlines() # lines
    #data = f.read().split("\n\n") # Paragraphs

test_data = """
"""

#data = test_data.splitlines()
#data = test_data


def solve(data):
    gamma = 0
    epsilon = ""
    for i in range(len(data[0])):
        gamma *= 2
        if len([1 for e in data if e[i] == '1']) > len(data)//2:
            gamma += 1
    return gamma * (2**(len(data[0]))-1-gamma)



def solve2(data):
    gen = [data[i] for i in range(len(data))]
    srub = [data[i] for i in range(len(data))]
    idx = 0
    while len(gen) > 1:
        c = 0
        d = 0
        for e in gen:
            if e[idx] == '1':
                c += 1
        if c >= len(gen)/2:
            gen = [gen[i] for i in range(len(gen)) if gen[i][idx] == '1']
        else:
            gen = [gen[i] for i in range(len(gen)) if gen[i][idx] == '0']
        idx += 1
    idx = 0
    while len(srub) > 1:
        c = 0
        for e in srub:
            if e[idx] == '1':
                c += 1
        if c >= len(srub)/2:
            srub = [srub[i] for i in range(len(srub)) if srub[i][idx] == '0']
        else:
            srub = [srub[i] for i in range(len(srub)) if srub[i][idx] == '1']
        idx += 1
    print(gen, srub)
    print(int(gen[0], 2))
    print(int(srub[0], 2))
    return int(gen[0], 2) * int(srub[0], 2)


first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
