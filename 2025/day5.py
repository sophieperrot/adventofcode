#!/usr/bin/env python3

"""
AOC 2025 Day 5: Cafeteria
https://adventofcode.com/2025/day/5
"""

# PART 1

fresh_ranges = {}

id_range = input()
while True:
    try:
        start, end = id_range.split("-")
        fresh_ranges[int(start)] = int(end)+1
        # print(fresh_ids)
        id_range = input()
    except Exception as e:
        # print(e)
        break

fresh_ids = set()
num_fresh = 0
while True:
    # print("yay2")
    try:
        id = int(input())
        # print(id)
        for i, start in enumerate(fresh_ranges):
            # print("yay")
            end = fresh_ranges[start]
            if id in range(start, end):
                # print("fresh", id)
                fresh_ids.add(id)
                # num_fresh += 1
    except Exception as e:
        # print(e)
        break

print(f"pt1 - number of fresh IDs: {len(fresh_ids)}")