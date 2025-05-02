#!/usr/bin/env python3

"""
AOC 2024 Day 4: Ceres Search
https://adventofcode.com/2024/day/[#]
"""

# PART 1

import re

word_search = []
count = 0

while True:
    try:
        line = input().split()
        word_search.append(line)
    except EOFError: # crt-D
        break

for row in word_search:
    matches = re.findall("(XMAS)|(SAMX)", row)
    count += len(matches)

num_rows = len(word_search)
row_len = len(word_search[0])

for j in range(num_rows):
    column = []
    for i in range(row_len):
        column.append(word_search[i][j])
    matches = re.findall("(XMAS)|(SAMX)", column)
    count += len(matches)



# print(f"pt1 - []: {}")


# PART 2

#print(f"pt2 - []: {}")
