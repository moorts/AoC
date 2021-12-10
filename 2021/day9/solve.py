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
2199943210
3987894921
9856789892
8767896789
9899965678
"""


#data = test_data.splitlines()
#data = test_data
#data = test_data.split("\n\n")

def min_neighbour(x, y, hm):
    res = 10
    for i in [-1, 1]:
        if x+i >= 0 and x+i < len(hm[0]):
            res = min(res, hm[y][x+i])
    for i in [-1, 1]:
        if y+i >= 0 and y+i < len(hm):
            res = min(res, hm[y+i][x])
    return res

def neighbours(x, y, hm, visited):
    n = []
    for i in [-1, 1]:
        if x+i >= 0 and x+i < len(hm[0]) and not visited[y][x+i]:
            if hm[y][x+i] != 9:
                n.append((x+i, y))
    for i in [-1, 1]:
        if y+i >= 0 and y+i < len(hm) and not visited[y+i][x]:
            if hm[y+i][x] != 9:
                n.append((x, y+i))
    return n



def solve(data):
    hm = [[int(c) for c in num] for num in data]
    res = 0
    for y in range(len(hm)):
        for x in range(len(hm[0])):
            if min_neighbour(x, y, hm) > hm[y][x]:
                res += hm[y][x] + 1
    return res


def solve2(data):
    hm = [[int(c) for c in num] for num in data]
    visited = [[False for _ in range(len(hm[0]))] for _ in range(len(hm))]
    sizes = []
    for y in range(len(hm)):
        for x in range(len(hm[0])):
            if visited[y][x] or hm[y][x] == 9:
                continue
            size = 1
            visited[y][x] = True
            stack = neighbours(x, y, hm, visited)
            print("--------")
            while stack:
                cx, cy = stack.pop(0)
                if visited[cy][cx]:
                    continue
                size += 1
                visited[cy][cx] = True
                stack.extend(neighbours(cx, cy, hm, visited))
            sizes.append(size)
    print(reduce(lambda a, b: a*b, sorted(sizes)[::-1][:3]))

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
