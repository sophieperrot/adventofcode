#!/usr/bin/env python3

"""
AOC 2024 Day 2: Red-Nosed Reports
https://adventofcode.com/2024/day/2
"""

# PART 1

reports = []

while True:
    try:
        report = [int(n) for n in input().split()]
        reports.append(report)
    except EOFError: # crt-D
        break

safe = len(reports)

for report in reports:
    if report != sorted(report) and report != sorted(report, reverse=True):
        safe -= 1
        continue
    for i in range(len(report) - 1):
        diff = abs(report[i+1] - report[i])
        if not (1 <= diff <= 3):
            safe -= 1
            break

print(f"pt1 - num of safe lists: {safe}")


# PART 2

def check_safe(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    for i in range(len(report) - 1):
        diff = abs(report[i+1] - report[i])
        if not (1 <= diff <= 3):
            return False
    return True

d_safe = len(reports)

for report in reports:
    if check_safe(report): continue
    marker = False
    for i in range(len(report)):
        if check_safe(report[:i]+report[i+1:]):
            marker = True
    if marker != True:
        d_safe -= 1

print(f"pt2 - dampened number of safe lists: {d_safe}")
