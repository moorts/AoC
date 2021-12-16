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
    data = f.read() # raw data
    #data = f.read().splitlines() # lines
    #data = f.read().split("\n\n") # Paragraphs

test_data = """\
9C0141080250320F1802104A08
"""


#test_data = test_data.splitlines()
test_data = test_data
#test_data = test_data.split("\n\n")

h = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
        '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
        'F': '1111' }


V = 0
idx = 0

def solve(data, part_2=False):
    global V, idx
    V = 0
    data = "".join([h[c] for c in data.replace("\n", "")])
    idx = 0
    sub = -1
    res = parse(data)
    return res if part_2 else V

from functools import reduce

fns = {
        0: sum,
        1: lambda ops: reduce(lambda x, y: x*y, ops),
        2: min,
        3: max,
        5: lambda ops: 1 if ops[0] > ops[1] else 0,
        6: lambda ops: 1 if ops[0] < ops[1] else 0,
        7: lambda ops: 1 if ops[0] == ops[1] else 0
    }

def decode_literal(data):
    global idx
    num = ""
    while data[idx] != '0':
        num += data[idx+1:idx+5]
        idx += 5
    num += data[idx+1:idx+5]
    idx += 5
    num = int(num, 2)
    return num

def decode_multiple(data, tid, n):
    ops = []
    for _ in range(n):
        op = parse(data)
        ops.append(op)
    return fns[tid](ops)

def decode_bits(data, tid, n):
    global idx
    old = idx
    ops = []
    while idx-old < n:
        op = parse(data)
        ops.append(op)
    return fns[tid](ops)

def parse(data):
    global V, idx
    version = int(data[idx:idx+3], 2)
    V += version
    tid = int(data[idx+3:idx+6], 2)
    idx += 6
    if tid == 4:
        return decode_literal(data)
    else:
        if data[idx] == '0':
            length = int(data[idx+1:idx+16], 2)
            idx += 16
            return decode_bits(data, tid, length)
        elif data[idx] == '1':
            n_pac = int(data[idx+1:idx+12], 2)
            idx += 12
            return decode_multiple(data, tid, n_pac)


first_result = solve(test_data)
second_result = solve(test_data, True)
print(f"TESTDATA Part 1: {first_result}")
print(f"TESTDATA Part 2: {second_result}")

first_result = solve(data)
second_result = solve(data, True)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
