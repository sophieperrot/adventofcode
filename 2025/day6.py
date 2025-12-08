#!/usr/bin/env python3

"""
AOC 2025 Day 5: Trash Compactor
https://adventofcode.com/2025/day/6
"""

# PART 1

scroll = input().split()

operators_start = min(scroll.index("*"), scroll.index("+"))
numbers = scroll[:operators_start]
operators = scroll[operators_start:]
num_problems = len(scroll) - operators_start

problems = {}
for i in range(num_problems):
    if operators[i] == "+":
        problems[i] = 0
    else:
        problems[i] = 1

q = 0
for number in numbers:
    if operators[q] == "+":
        problems[q] += int(number)
    else:
        problems[q] *= int(number)
    q = (q+1) % num_problems

sum = 0
for problem in problems.values():
    sum += problem

print(f"pt1 - grand total: {sum}")