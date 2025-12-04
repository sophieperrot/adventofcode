#!/usr/bin/env python3

"""
AOC 2025 Day 2: Gift Shop
https://adventofcode.com/2025/day/2
"""

# PART 1

id_list = input().split(",")
invalid_ids = 0

def is_invalid(id: str):
    id_mid = len(id) // 2
    if id[:id_mid] == id[id_mid:]:
        return True
    return False

id_range_list = []
for id_range in id_list:
    id_range_list.append((int(id_range.split("-")[0]), int(id_range.split("-")[1]) + 1))

for lower_bound, upper_bound in id_range_list:
    for id in range(lower_bound, upper_bound):
        if is_invalid(str(id)): invalid_ids += id

print(f"pt1 - invalid IDs sum: {invalid_ids}")


# PART 2

invalid_ids = 0

def new_is_invalid(id: str, unit_len: int):
    repeats = unit_len * (len(id) // unit_len - 1)
    for i in range(0, repeats, unit_len):
        try:
            if id[i:i+unit_len] != id[i+unit_len:i+2*unit_len]:
                return False
        except:
            break
    return True

for lower_bound, upper_bound in id_range_list:
    for id in range(lower_bound, upper_bound):
        middle = len(str(id)) // 2 + 1
        for i in range(1, middle):
            if len(str(id)) % i == 0 and new_is_invalid(str(id), i):
                invalid_ids += id
                break

print(f"pt2 - new invalid IDs sum: {invalid_ids}")