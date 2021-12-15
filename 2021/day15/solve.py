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
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


test_data = test_data.splitlines()
#test_data = test_data
#test_data = test_data.split("\n\n")

def neighbors(r, c, grid):
    out = []
    if r+1 < len(grid):
        out.append((r+1, c))
    if c+1 < len(grid):
        out.append((r, c+1))
    if r > 0:
        out.append((r-1, c))
    if c > 0:
        out.append((r, c-1))
    return out

from collections import defaultdict

def solve(data):
    grid = [[int(c) for c in line] for line in data]
    visited = set()
    distances = defaultdict(int)
    distances[(0, 0)] = 0
    unvisited = {(0, 0)}
    current = (0, 0)
    while ((len(grid)-1, len(grid[0])-1)) not in visited:
        current = min(unvisited, key=lambda x: distances[x])
        for r, c in neighbors(current[0], current[1], grid):
            if ((r, c)) in visited:
                continue
            if (r, c) in distances:
                distances[(r,c)] = min(distances[(r, c)], distances[current] + grid[r][c])
            else:
                distances[(r,c)] = distances[current] + grid[r][c]
                unvisited.add((r, c))
        visited.add(current)
        unvisited.remove(current)
    return distances[(len(grid)-1, len(grid[0])-1)]




import heapq

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

def solve2(data):
    grid = [[int(c) for c in line] for line in data]
    dim = len(grid)
    n_tiles = 5
    distances = [[None for _ in range(dim*n_tiles)] for _ in range(dim*n_tiles)]
    unvisited = [(0, 0, 0)]
    assert(len(grid) == len(grid[0]))
    while unvisited:
        D, r, c = heapq.heappop(unvisited)
        if r>=dim*n_tiles or r<0 or c<0 or c>=dim*n_tiles:
            continue

        val = grid[r%dim][c%dim] + r//dim + c//dim
        val = val - 9 if val > 9 else val
        n_dist = val + D
        if distances[r][c] == None or n_dist < distances[r][c]:
            distances[r][c] = n_dist
        else:
            continue
        if r == n_tiles*dim-1 and c == n_tiles*dim-1:
            break

        for i in range(4):
            rr = r + DR[i]
            cc = c + DC[i]
            heapq.heappush(unvisited, (distances[r][c], rr, cc))
    return distances[dim*n_tiles-1][dim*n_tiles-1] - grid[0][0]

first_result = solve(test_data)
second_result = solve2(test_data)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
