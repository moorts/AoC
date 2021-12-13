
from parse import parse
p = "Step {} must be finished before step {} can begin."

with open('./input') as f:
    data = f.read().splitlines()

test_data = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

#data = test_data.splitlines()

order = ""
#available = {}
from collections import defaultdict

rules = defaultdict(set)
steps = set()
for line in data:
    before, after = parse(p, line)
    rules[before].add(after)
    steps.add(before)

print(rules)

required = defaultdict(set)

start = steps.copy()
for k, v in rules.items():
    for x in v:
        required[x].add(k)
    start -= v

available = start

done = set()
in_progress = set()

time = 0
workers = [[0, ""] for _ in range(5)]
print(workers)

while available:
    selected = ""
    for x in sorted(list(available)):
        if x in in_progress:
            continue
        if required[x] - done == set():
            for w in workers:
                if w[0] == -1:
                    w[0] = 60 + (ord(x) - ord('A') + 1)
                    print(w[0])
                    w[1] = x
                    in_progress.add(x)
                    break
    #if len(available - in_progress) == 0:
    seconds_working = min(filter(lambda x: x[0] != -1, workers), key=lambda x: x[0])[0]
    #else:
    workers = [[w[0]-seconds_working, w[1]] if w[0] >= 0 else [w[0], w[1]] for w in workers]
    time += seconds_working
    for w in workers:
        if w[0] == 0:
            order += str(w[1])
            available |= rules[w[1]]
            done.add(w[1])
            available -= done
            in_progress -= {w[1]}
            w[0] = -1
    print(workers)
print(time)

