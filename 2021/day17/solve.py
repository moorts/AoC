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
target area: x=20..30, y=-10..-5
"""


#test_data = test_data.splitlines()
test_data = test_data
#test_data = test_data.split("\n\n")

from math import sqrt

def solve(data, part_2=False):
    x, y = 0, 0
    xmin, xmax, ymin, ymax = ints(list(parse("target area: x={}..{}, y={}..{}", data)))
    highest = -1000000
    stuff = set()
    for vx in range(xmax+1):
        for vy in range(ymin, abs(ymin)):
            x, y = 0, 0
            cvx = vx
            cvy = vy
            my = y
            while x <= xmax and y >= ymin:
                x += cvx
                y += cvy
                cvy -= 1
                if cvx > 0:
                    cvx -= 1
                elif cvx < 0:
                    cvx += 1
                my = max(my, y)
                if x >= xmin and y <= ymax and x <= xmax and y >= ymin:
                    highest = max(highest, my)
                    stuff.add((vx, vy))
    return highest if not part_2 else len(stuff)
    


first_result = solve(test_data)
second_result = solve(test_data, True)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")

first_result = solve(data)
second_result = solve(data, True)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
