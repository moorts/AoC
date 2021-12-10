import subprocess

import numpy as np
from functools import *
from parse import parse

year = 2021
day = 1

def ints_it(it):
    while it:
        yield int(it.pop(0))

def ints(it):
    return list(ints_it(it))

with open('./input') as f:
    data = ints(f.read().splitlines()) # raw data
    #data = f.read().splitlines() # lines
    #data = f.read().split(\"\\n\\n\") # Paragraphs

def solve(data):
    return len([0 for i in range(len(data)-1) if data[i+1] > data[i]])

def solve2(data):
    return len([0 for i in range(len(data)-3) if sum(data[i+1:i+4]) > sum(data[i:i+3])])


result = solve(data)
print((lambda data: len([0 for i in range(len(data)-1) if int(data[i+1]) > int(data[i])]))(open('./input').read().splitlines()))
print(result)
