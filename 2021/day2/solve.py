import subprocess

import numpy as np
from functools import *
from parse import parse

year = 2021
day = 2

def ints_it(it):
    while it:
        yield int(it.pop(0))

def ints(it):
    return list(ints_it(it))


with open('./input') as f:
    data = f.read().splitlines() # raw data
    #data = f.read().splitlines() # lines
    #data = f.read().split(\"\\n\\n\") # Paragraphs


def solve(data):
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
    return x * depth






result = solve(data)
print(result)
