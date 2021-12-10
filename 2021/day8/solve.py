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
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


#data = test_data.splitlines()
#data = test_data
#data = test_data.split("\n\n")


def solve(data):
    lines = [line.split(" | ") for line in data]
    c = 0
    for line in lines:
        _, output = line
        for entry in output.split(" "):
            if len(entry) in [2, 4, 3, 7]:
                c += 1
    return c
    

def rev(d):
    out = dict()
    for k, v in d.items():
        out[v] = k

def eq(s, pat, segs):
    if len(s) != len(pat):
        return False
    for c in s:
        if segs[c] not in pat:
            return False
    return True


def solve2(data):
    lines = [line.split(" | ") for line in data]
    res = 0
    for line in lines:
        pattern, output = line
        digits = dict()
        for entry in pattern.split(" "):
            if len(entry) == 2:
                digits[1] = set(entry)
            elif len(entry) == 3:
                digits[7] = set(entry)
            elif len(entry) == 4:
                digits[4] = set(entry)
            elif len(entry) == 7:
                digits[8] = set(entry)
        segments = dict()
        segments['a'] = list(digits[7] - digits[1])[0]
        b_and_d = digits[4] - digits[1]
        for entry in pattern.split(" "):
            pat = set(entry) - digits[4]
            if len(pat) == 2:
                segments['g'] = list(pat - set(segments['a']))[0]
                if len(entry) == 6:
                    digits[9] = set(entry)
        for entry in pattern.split(" "):
            pat = set(entry) - digits[4] - set([segments['a'], segments['g']])
            if len(pat) == 1 and len(entry) == 6:
                segments['e'] = list(pat)[0]
                f = set(entry) - b_and_d - set([segments['a'], segments['g'], segments['e']])
                if len(f) == 1:
                    digits[6] = set(entry)
                    segments['f'] = list(f)[0]
                    segments['c'] = list(digits[1] - f)[0]
                    print(segments['c'], segments['f'])
                else:
                    digits[0] = set(entry)
        for entry in pattern.split(" "):
            pat = set(entry) - digits[0]
            if len(pat) == 1:
                segments['d'] = list(pat)[0]
                segments['b'] = list(b_and_d - pat)[0]
                if eq("abdfg", set(entry), segments):
                    digits[5] = set(entry)
        for entry in pattern.split(" "):
            if eq("acdeg", entry, segments):
                digits[2] = set(entry)
            if eq("acdfg", entry, segments):
                digits[3] = set(entry)
        out = ""
        for val in output.split(" "):
            for k, v in digits.items():
                if set(val) == v:
                    out += str(k)
        res += int(out)
        print(digits[9])

    return res

#data = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf".splitlines()

def solve2(data):
    lines = [list(map(lambda x: [set(p) for p in x.split(" ")], line.split(" | "))) for line in data]
    res = 0
    for line in lines:
        pattern, output = line
        digits = dict()
        one = filter(lambda x: len(x) == 2, pattern)
        four = next(filter(lambda x: len(x) == 4, pattern))
        seven = next(filter(lambda x: len(x) == 3, pattern))
        eight = next(filter(lambda x: len(x) == 7, pattern))
        len_5 = list(filter(lambda x: len(x) == 5, pattern))
        three = next(filter(lambda x: len(x-one) == 3, len_5))
        len_5.remove(three)
        two = next(filter(lambda x: len(x-four) == 3, len_5))
        len_5.remove(two)
        five = len_5[0]
        len_6 = list(filter(lambda x: len(x) == 6, pattern))
        six = next(filter(lambda x: len(x-one) == 5, len_6))
        len_6.remove(six)
        nine = next(filter(lambda x: len(x-three) == 1, len_6))
        len_6.remove(nine)
        zero = len_6[0]
        m = [zero, one, two, three, four, five, six, seven, eight, nine]
        n = 0
        for p in output:
            for i, v in enumerate(m):
                if v == set(p):
                    n *= 10
                    n += i
        res += n
    return res

first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
