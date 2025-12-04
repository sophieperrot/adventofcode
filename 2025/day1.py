#!/usr/bin/env python3

"""
AOC 2025 Day 1: Secret Entrance
https://adventofcode.com/2025/day/1
"""

# PART 1

dial_pos = 50
password = 0

while True:
    try:
        move = input().strip()
        if move[0] == "L":
            dial_pos = (dial_pos - int(move[1:])) % 100
        elif move[0] == "R":
            dial_pos = (dial_pos + int(move[1:])) % 100
        if dial_pos == 0:
            password += 1
    except:
        break

print(f"pt1 - password: {password}")