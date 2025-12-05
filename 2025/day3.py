#!/usr/bin/env python3

"""
AOC 2024 Day 3: Lobby
https://adventofcode.com/2025/day/3
"""

# PART 1

total_joltage = 0

while True:
    try:
        bank = [int(i) for i in input().strip()]
        max_jolt = ""
        first_digit = max(bank[:-1])
        second_digit = max(bank[bank.index(first_digit)+1:])
        max_jolt = str(first_digit) + str(second_digit)
        total_joltage += int(max_jolt)
    except:
        break

print(f"pt1 - total output joltage: {total_joltage}")