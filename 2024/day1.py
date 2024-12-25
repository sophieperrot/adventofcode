#!/usr/bin/env python3

"""
AOC 2024 Day 1: Historian Hysteria
https://adventofcode.com/2024/day/1
"""

# PART 1

left_list = []
right_list = []

while True:
    try:
       l, r = input().split()
       left_list.append(int(l))
       right_list.append(int(r))
    except:
        break

left_list.sort()
right_list.sort()

list_len = len(left_list)
distance = 0

for i in range(list_len):
    distance += abs(left_list[i] - right_list[i])

print(f"pt1 - distance between lists: {distance}")


# PART 2

similarity = 0

def find_freq(n):
    freq = 0
    for num in right_list:
        if num == n: freq += 1
    return freq

for num in left_list:
    similarity += num * find_freq(num)

print(f"pt2 - similarity score: {similarity}")
