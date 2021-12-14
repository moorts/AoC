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
    mx = max(counts.values())
    mn = min(counts.values())
    return mx - mn




from math import ceil


def solve2(data):
    template, rules = data
    rules_raw = rules.splitlines()
    rules = defaultdict(str)
    for rule in rules_raw:
        pair, insertion = rule.split(" -> ")
        rules[pair] = insertion
    polymer = template
    pairs = defaultdict(int)
    chars = Counter(polymer)
    first = polymer[:2]
    last = polymer[-2:]
    for i in range(len(polymer)-1):
        pairs[polymer[i:i+2]] += 1
    for _ in range(40):
        nd = defaultdict(int)
        for pair, c in pairs.items():
            if pair in rules:
                pairs[pair] = 0
                r = rules[pair]
                nd[pair[0] + r] += c
                nd[r + pair[1]] += c
                chars[r] += c
        pairs.update(nd)

    counts = Counter()

    for k, v in pairs.items():
        counts[k[0]] += v / 2
        counts[k[1]] += v / 2
    values = [ceil(count) for count in counts.values()]
    mx = max(values)
    m = min(values)


    return mx - m

first_result = solve(test_data)
second_result = solve2(test_data)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
