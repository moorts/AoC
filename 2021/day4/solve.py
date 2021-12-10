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

test_data = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

#data = test_data.splitlines()
#data = test_data
#                        won[num] = True
#data = test_data.split("\n\n")


class Board:

    def __init__(self, board):
        self.board = board
        self.marked = [[False for _ in range(5)] for _ in range(5)]
        self.won = False

    def check_won(self):
        for i in range(5):
            if all(self.marked[i]):
                self.won = True
                return True
            if all([self.marked[x][i] for x in range(5)]):
                self.won = True
                return True
        return False

    def unmarked(self):
        unmarked = 0
        for j in range(5):
            for k in range(5):
                if not self.marked[j][k]:
                    unmarked += int(self.board[j][k])
        return unmarked


    def mark(self, x):
        if self.won:
            return -1

        for i in range(5):
            if x in self.board[i]:
                self.marked[i][self.board[i].index(x)] = True
                if self.check_won():
                    return self.unmarked() * int(x)
        return -1

def solve(data):
    draws = data[0].split(",")
    boards = [Board([line.split() for line in board.splitlines()]) for board in data[1:]]
    for d in draws:
        for board in boards:
            res = board.mark(d)
            if res != -1:
                return res

def solve2(data):
    draws = data[0].split(",")
    boards = [Board([line.split() for line in board.splitlines()]) for board in data[1:]]
    last = 0
    for d in draws:
        for board in boards:
            res = board.mark(d)
            if res != -1:
                last = res
    return last





first_result = solve(data)
second_result = solve2(data)
print(f"Part 1: {first_result}")
print(f"Part 2: {second_result}")
