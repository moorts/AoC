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
    #data = f.read().splitlines() # lines
    data = f.read().split("\n\n") # Paragraphs

test_data = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


#test_data = test_data.splitlines()
#test_data = test_data
test_data = test_data.split("\n\n")


def solve(data, part_2=False):
    cords, folds = data[0].splitlines(), data[1].splitlines()
    dots = set()
    for c in cords:
        x, y = list(map(int, c.split(",")))
        dots.add((x, y))
    if not part_2:
        folds = [folds[0]]
    for fold in folds:
        axis, val = fold.split(" ")[2].split("=")
        val = int(val)
        res = set()
        for x, y in dots:
            if axis == 'x':
                new = (val - (x - val))
                res.add((min(new, x), y))
            elif axis == 'y':
                new = (val - (y - val))
                res.add((x, min(y, new)))

        dots = res

    if part_2:
        mx = max(dots, key=lambda x: x[0])[0]
        my = max(dots, key=lambda x: x[1])[1]
        for y in range(my+1):
            row = ""
            for x in range(mx+1):
                if (x, y) in dots:
                    row += '#'
                else:
                    row += '.'
            print(row)
    else:
        return len(res)


def solve2(data):
    pass

#first_result = solve(test_data)
#second_result = solve2(test_data)
#print(f"TESTDATA Part 1: {first_result}")
#print(f"TESTDATA Part 2: {second_result}")

print("---------------------------------")

first_result = solve(data)
print(f"Part 1: {first_result}")
second_result = solve(data, True)
#print(f"Part 2: {second_result}")
