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
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


#data = test_data.splitlines()
#data = test_data
#data = test_data.split("\n\n")

def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if x+dx < 0 or x+dx > 9:
                continue
            elif y+dy < 0 or y+dy > 9:
                continue
            yield (x+dx, y+dy)

def solve(data):
    grid = [[int(x) for x in line] for line in data]
    total = 0
    i = 0
    for i in range(100):
        i += 1
        # Add one to all
        flashes = []
        for y in range(10):
            for x in range(10):
                grid[y][x] += 1
                if grid[y][x] > 9:
                    flashes.append((y, x))
        energize = flashes[:]
        while energize:
            y, x = energize.pop(0)
            for nx, ny in neighbors(x, y):
                grid[ny][nx] += 1
                if grid[ny][nx] > 9:
                    if (ny, nx) not in flashes:
                        flashes.append((ny, nx))
                        energize.append((ny, nx))
        for y, x in flashes:
            grid[y][x] = 0
        total += len(flashes)
    return total




def solve2(data):
    grid = [[int(x) for x in line] for line in data]
    total = 0
    i = 0
    while True:
        i += 1
        # Add one to all
        flashes = []
        for y in range(10):
            for x in range(10):
                grid[y][x] += 1
                if grid[y][x] > 9:
                    flashes.append((y, x))
        energize = flashes[:]
        while energize:
            y, x = energize.pop(0)
            for nx, ny in neighbors(x, y):
                grid[ny][nx] += 1
                if grid[ny][nx] > 9:
                    if (ny, nx) not in flashes:
                        flashes.append((ny, nx))
                        energize.append((ny, nx))
        if len(set(flashes)) == 100:
            return i
        for y, x in flashes:
            grid[y][x] = 0
        total += len(flashes)
    return total

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
