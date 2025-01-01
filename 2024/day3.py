#!/usr/bin/env python3

"""
AOC 2024 Day 3: Mull It Over
https://adventofcode.com/2024/day/3
"""

# PART 1

import re

memory = input()
uncorrupted = re.findall("mul\(\d+,\d+\)", memory)

result = 0
for instruction in uncorrupted:
    n, m = instruction[4:-1].split(",")
    result += int(n) * int(m)

print(f"pt1 - sum of uncorrupted instructions: {result}")


# PART 2

new_uncorrupted = re.findall("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", memory)

new_result = 0
enabled = True
for instruction in new_uncorrupted:
    if "don't()" in instruction:
        enabled = False
        continue
    elif "do()" in instruction:
        enabled = True
        continue
    if enabled:
        n, m = instruction[0][4:-1].split(",")
        new_result += int(n) * int(m)

print(f"pt2 - sum of enabled instructions: {new_result}")
