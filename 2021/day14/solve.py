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
    #data = f.read().splitlines() # lines
    data = f.read().split("\n\n") # Paragraphs

test_data = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


#test_data = test_data.splitlines()
#test_data = test_data
test_data = test_data.split("\n\n")

from collections import defaultdict

from collections import Counter

def solve(data):
    template, rules = data
    rules_raw = rules.splitlines()
    rules = defaultdict(str)
    for rule in rules_raw:
        pair, insertion = rule.split(" -> ")
        rules[pair] = insertion
    polymer = template
    for _ in range(10):
        np = ""
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            if pair in rules:
                np += polymer[i] + rules[pair]
            else:
                np += polymer[i]
        np += polymer[-1]
        polymer = np
    counts = Counter(polymer)
    mx, m = 0, -1
    for k, v in counts.items():
        mx = max(mx, v)
        if m == -1:
            m = v
        else:
            m = min(m, v)
    return mx - m






def solve2(data):
    template, rules = data
    rules_raw = rules.splitlines()
    rules = defaultdict(str)
    for rule in rules_raw:
        pair, insertion = rule.split(" -> ")
        rules[pair] = insertion
    polymer = template
    pairs = defaultdict(int)
    chars = defaultdict(int)
    for c in polymer:
        chars[c] += 1
    for i in range(len(polymer)-1):
        pairs[polymer[i:i+2]] += 1
    print(pairs)
    for _ in range(40):
        np = set()
        nd = defaultdict(int)
        print(len(pairs))
        for pair, c in pairs.items():
            if pair in rules:
                pairs[pair] = 0
                r = rules[pair]
                nd[pair[0] + r] += c
                nd[r + pair[1]] += c
                chars[r] += c
        for k, v in nd.items():
            pairs[k] += v

    counts = Counter(chars)

    mx, m = 0, -1
    for k, v in counts.items():
        mx = max(mx, v)
        if m == -1:
            m = v
        else:
            m = min(m, v)
    return mx - m

first_result = solve(test_data)
second_result = solve2(test_data)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
