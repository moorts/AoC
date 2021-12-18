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
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""


test_data = test_data.splitlines()
#test_data = test_data
#test_data = test_data.split("\n\n")


from itertools import permutations

def solve(data, part_2=False):
    snails = [eval(line) for line in data]
    if not part_2:
        s = snails[0]
        for snail in snails[1:]:
            s = add(s, snail)
            while True:
                if explodes(s, 0)[0]:
                    continue
                else:
                    if split(s):
                        continue
                    break
        return mag(s)
    else:
        m = 0
        pm = []
        for s1 in snails:
            for s2 in snails:
                if s1 == s2:
                    continue
                s = add(copy(s1), copy(s2))
                while True:
                    if explodes(s, 0)[0]:
                        continue
                    else:
                        if split(s):
                            continue
                        break
                m = max(m, mag(s))
        return m

def copy(s):
    if type(s) != list:
        return s
    return [copy(s[0]), copy(s[1])]

def mag(t):
    if type(t) != list:
        return t
    return 3*mag(t[0]) + 2*mag(t[1])


def add(a, b):
    return [a, b]

def reduce(n):
    t = n
    level = 1
    # Check for explosion
    q = [(n, 0)]
    while q:
        c = q.pop(0)
        if c[1] == 3:
            pass

def leaves(t):
    s = [t]
    out = []
    while s:
        c = s.pop()
        if type(c) == list:
            s.append(c[1])
            s.append(c[0])
        else:
            out.append(c)
    return out

def explodes(t, level):
    if level == 4:
        if type(t) == list:
            return (True, t[0], t[1])
        return (False, 0, 0)
    if type(t) != list:
        return (False, 0, 0)
    left = explodes(t[0], level+1)
    if left[0]:
        if level == 3:
            t[0] = 0
        if left[2] != -1:
            if update_right(t, left[2]):
                return (True, left[1], -1)
        return (True, left[1], left[2])
    right = explodes(t[1], level+1)
    if right[0]:
        if level == 3:
            t[1] = 0
        if right[1] != -1:
            if update_left(t, right[1]):
                return (True, -1, right[2])
        return (True, right[1], right[2])
    return (False, 0, 0)

def update_right(t, v):
    if type(t[1]) != list:
        t[1] += v
        return True
    s = [t[1]]
    while s:
        c = s.pop()
        if type(c[0]) != list:
            c[0] += v
        else:
            s.append(c[0])
    return True

def update_left(t, v):
    if type(t[0]) != list:
        t[0] += v
        return True
    s = [t[0]]
    while s:
        c = s.pop()
        if type(c[1]) != list:
            c[1] += v
        else:
            s.append(c[1])
    return True

from math import ceil

def split(t):
    if type(t[0]) != list:
        if t[0] >= 10:
            t[0] = [t[0]//2, ceil(t[0]/2)]
            return True
        else:
            if type(t[1]) != list:
                if t[1] >= 10:
                    t[1] = [t[1]//2, ceil(t[1]/2)]
                    return True
                return False
            else:
                return split(t[1])
    elif not split(t[0]):
        if type(t[1]) != list:
            if t[1] >= 10:
                t[1] = [t[1]//2, ceil(t[1]/2)]
                return True
            return False
        else:
            return split(t[1])
    return True



first_result = solve(test_data)
second_result = solve(test_data, True)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")

first_result = solve(data)
second_result = solve(data, True)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
