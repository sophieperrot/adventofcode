#!/usr/bin/env python3

"""
AOC 2025 Day 5: Cafeteria
https://adventofcode.com/2025/day/5
"""

# PART 1

fresh_ids = set()

id_range = input()
while True:
    try:
        start = int(id_range.split("-")[0])
        end = int(id_range.split("-")[1]) + 1
        for i in range(start, end):
            fresh_ids.add(i)
        id_range = input()
    except Exception as e:
        # print(e)
        break

num_fresh = 0
while True:
    try:
        id = int(input())
        if id in fresh_ids:
            num_fresh += 1
    except Exception as e:
        # print(e)
        break

print(f"pt1 - number of fresh IDs: {num_fresh}")