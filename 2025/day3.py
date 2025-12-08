#!/usr/bin/env python3

"""
AOC 2024 Day 3: Lobby
https://adventofcode.com/2025/day/3
"""

# PART 1

banks = []
total_joltage = 0

def max_joltage(bank: list, n: int):
    # digits = []
    max_jolt = ""
    marker = 0
    for i in range(n, 0, -1):
        print(i)
        end_marker = (-i+1 if i>1 else None)
        try:
            digit = max(bank[marker:end_marker])
        except:
            break
        max_jolt += str(digit)
        marker = bank.index(digit) + 1
        print(f"digit: {digit}, marker: {marker}, max jolt: {max_jolt}")
    # max_jolt = [str(digit) for digit in digits]
    # total_joltage += int(max_jolt)
    # print(max_jolt)
    return max_jolt

while True:
    try:
        bank = [int(i) for i in input().strip()]
        # banks.append(bank)
        total_joltage += int(max_joltage(bank, 2))
    except Exception as e:
        break

print(f"pt1 - total output joltage: {total_joltage}")


# PART 2

total_joltage = 0

for bank in banks:
    print(bank)
    total_joltage += int(max_joltage(bank, 12))

print(f"pt2 - new total output joltage: {total_joltage}")
