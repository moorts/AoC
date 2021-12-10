import subprocess

import numpy as np
from functools import *
from parse import parse

year = 2018
day = 5

with open('./input') as f:
    data = f.read().rstrip() # raw data
    #data = f.read().splitlines() # lines
    #data = f.read().split(" ") # Paragraphs

def solve(data):
    m = len(data)
    for c in set(data.lower()):
        polymer = ''.join(filter(lambda x: x.lower() != c, data))
        reacted = react(polymer)
        old = polymer
        while reacted != old:
            old = reacted
            reacted = react(reacted)
        if len(reacted) < m:
            m = len(reacted)
    return m

def react(polymer):
    i = 0
    out = ""
    while i < len(polymer):
        if i == len(polymer)-1:
            out += polymer[i]
            break
        if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
            # react
            i += 1
        else:
            out += polymer[i]
        i += 1
    return out


result = solve(data)
print(result)
#print(''.join(set(data.lower())))
#subprocess.run(["aerondight", "-s", str(year), str(day), str(result)])
