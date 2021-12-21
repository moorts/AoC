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
"""


test_data = test_data.splitlines()
#test_data = test_data
#test_data = test_data.split("\n\n")


def solve(data):
    p1 = int(parse("Player 1 starting position: {}", data[0])[0])
    p2 = int(parse("Player 2 starting position: {}", data[1])[0])
    s1 = 0
    s2 = 0
    die = 1
    turn = True #true if p1 else false
    rolls = 0
    while True:
        total = 3*die + 3
        rolls += 3
        die = ((die + 2) % 100) + 1
        if turn:
            p1 = ((p1 - 1 + total) % 10) + 1
            s1 += p1
        else:
            p2 = ((p2 - 1 + total) % 10) + 1
            s2 += p2
        turn = not turn
        if s1 >= 1000:
            return s2 * rolls
        elif s2 >= 1000:
            return s1 * rolls


    


from collections import defaultdict

def solve2(data):
    p1 = int(parse("Player 1 starting position: {}", data[0])[0])
    p2 = int(parse("Player 2 starting position: {}", data[1])[0])
    return max(play(p1, p2, 0, 0, True))

from itertools import *
import functools

temp = [list(range(1,4)) for _ in range(3)]
dice = list(map(sum, product(*temp)))

@functools.cache
def play(p1, p2, s1, s2, turn):
    if s1 >= 21:
        return (1, 0)
    elif s2 >= 21:
        return (0, 1)
    rs = []
    for d in dice:
        new_p1 = ((p1 - 1 + d*turn) % 10) + 1
        new_p2 = ((p2 - 1 + d*(1-turn)) % 10) + 1
        rs.append(play(new_p1, new_p2, s1 + new_p1*turn, s2 + new_p2*(1-turn), not turn))
    return sum([x[0] for x in rs]), sum([x[1] for x in rs])





"""
first_result = solve(test_data)
second_result = solve2(test_data)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")
"""

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
