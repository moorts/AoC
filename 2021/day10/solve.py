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
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


#data = test_data.splitlines()
#data = test_data
#data = test_data.split("\n\n")

scores = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
opening = { '(', '[', '<', '{' }
matching = { '(': ')', '[': ']', '{': '}', '<': '>' }

print(len(data))

def solve(data):
    res = 0
    corrupt = []
    for line in data:
        stack = []
        for c in line:
            if c in opening:
                stack.append(c)
            else:
                if matching[stack.pop()] != c:
                    corrupt.append(line)
                    res += scores[c]
    for c in corrupt:
        data.remove(c)
    return res


values = { '(': 1, '[': 2, '{': 3, '<': 4 }

def solve2(data):
    scores = []
    for line in data:
        stack = []
        for c in line:
            if c in opening:
                stack.append(c)
            else:
                stack.pop()
        if stack:
            scores.append(reduce(lambda a, b: (a*5) + b, map(lambda x: values[x], stack[::-1])))
    return sorted(scores)[len(scores)//2]


first_result = solve(data)
print(len(data))
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
