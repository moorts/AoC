print("test")
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
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""


test_data = test_data.splitlines()
#test_data = test_data
#test_data = test_data.split("\n\n")


def solve(data):
    caves = dict()
    big = set()
    for line in data:    
        src, dst = line.split("-")
        if src in caves:
            caves[src].append(dst)
        else:
            caves[src] = [dst]
        if dst in caves:
            caves[dst].append(src)
        else:
            caves[dst] = [src]
        if dst != dst.lower():
            big.add(dst)
    print(caves)
    stack = [('start', 1)]
    path = []
    paths = []
    while stack:
        curr, back = stack.pop()
        if curr == 'end':
            paths.append(path.copy())
            continue

        
        path = path[:back]
        path.append(curr)

        if curr not in caves:
            path.pop()
            continue
        l = len(stack)
        for cave in caves[curr]:
            if cave.islower():
                if cave not in path:
                    stack.append((cave, len(path)))
            else:
                stack.append((cave, len(path)))
        if l == len(stack):
            path.pop()
    return len(paths)




def solve2(data):
    caves = dict()
    small = set()
    for line in data:    
        src, dst = line.split("-")
        if src in caves:
            caves[src].append(dst)
        else:
            caves[src] = [dst]
        if dst in caves:
            caves[dst].append(src)
        else:
            caves[dst] = [src]
        if dst.islower():
            small.add(dst)
        if src.islower():
            small.add(src)
    stack = [('start', 1)]
    path = []
    paths = []
    while stack:
        curr, back = stack.pop()
        if curr == 'end':
            paths.append(path.copy())
            continue

        
        path = path[:back]
        path.append(curr)

        if curr not in caves:
            path.pop()
            continue
        l = len(stack)
        for cave in caves[curr]:
            if cave.islower():
                if cave not in path:
                    stack.append((cave, len(path)))
                elif cave != 'start' and path.count(cave) == 1:
                    for s in small:
                        if path.count(s) == 2:
                            break
                    else:
                        stack.append((cave, len(path)))
            else:
                stack.append((cave, len(path)))
        if l == len(stack):
            path.pop()
    return len(paths)

first_result = solve(test_data)
second_result = solve2(test_data)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
