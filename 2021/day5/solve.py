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

test_data = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

#data = test_data.splitlines()
#data = test_data
#data = test_data.split("\n\n")


def solve(data):
    points = dict()
    for line in data:
        start, end = line.split(" -> ")
        start, end = tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))
        # vertical line
        if start[0] == end[0]:
            s, e = start[1], end[1]
            if start[1] > end[1]:
                s, e = e, s

            for y in range(s, e+1):
                point = (start[0], y)
                if point in points:
                    points[point] += 1
                else:
                    points[point] = 1
        elif start[1] == end[1]:
            s, e = start[0], end[0]
            if start[0] > end[0]:
                s, e = end[0], start[0]

            for x in range(s, e+1):
                point = (x, start[1])
                if point in points:
                    points[point] += 1
                else:
                    points[point] = 1
        else:
            sx, ex = start[0], end[0]
            sy, ey = start[1], end[1]
            nx = 1
            ny = 1
            if start[0] > end[0]:
                nx = -1
            if start[1] > end[1]:
                ny = -1
            for delta in range(abs(ex - sx) + 1):
                point = (sx+delta*nx, sy+delta*ny)
                if point in points:
                    points[point] += 1
                else:
                    points[point] = 1

    return len(list(filter(lambda x: x > 1, points.values())))



def solve2(data):
    pass


first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
