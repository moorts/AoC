import subprocess

import numpy as np
from functools import *
from parse import parse
import datetime

year = 2018
day = 4

with open('./input') as f:
    #data = f.read() # raw data
    data = f.read().splitlines() # lines
    #data = f.read().split(" ") # Paragraphs

def chrono(data):
    return sorted(data, key=lambda x: datetime.datetime.strptime(parse("[{}]{}", x)[0], "%Y-%m-%d %H:%M"))

def solve(data):
    lines = chrono(data)
    guards = dict()
    guard = ""
    current = []
    start = 0;
    end = 0
    idx = 0
    asleep = 0
    for line in lines:
        if line.find("#") != -1:
            if guard != "":
                if asleep == 0:
                    current.extend([asleep for _ in range(60-end)])
                else:
                    current.extend([asleep for _ in range(60-start)])
                if guard in guards:
                    guards[guard].append(current)
                else:
                    guards[guard] = [current]
            _, minute, guard = parse("[{}:{}] Guard #{} begins shift", line)
            start = int(minute)
            end = 0
            current = []
            asleep = 0
        elif line.find("falls asleep") != -1:
            asleep = 1
            _, minute, _ = parse("[{}:{}]{}", line)
            start = int(minute)
            current.extend([0 for _ in range(start-end)])
        elif line.find("wakes up") != -1:
            asleep = 0
            _, e, _ = parse("[{}:{}]{}", line)
            end = int(e)
            current.extend([1 for _ in range(end-start)])
        idx += 1
    if asleep == 0:
        current.extend([asleep for _ in range(60-end)])
    else:
        current.extend([asleep for _ in range(60-start)])
    if guard in guards:
        guards[guard].append(current)
    else:
        guards[guard] = [current]
    max_guard = ""
    max_minutes = 0
    max_idx = 0
    max_count = 0
    for key, value in guards.items():
        minutes = sum(map(lambda x: sum(x), value))
        if minutes > max_minutes:
            max_minutes = minutes
        counts = [0 for _ in range(60)]
        for v in value:
            for i, val in enumerate(v):
                counts[i] += val
        for i, c in enumerate(counts):
            if c > max_count:
                max_count = c
                max_guard = key
                max_idx = i
    return max_idx * int(max_guard)




result = str(solve(data))
print(result)
#subprocess.run(["aerondight", "-s", str(year), str(day), result])
