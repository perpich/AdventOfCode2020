from os import path
from collections import Counter
import re


with open(path.join(path.dirname(__file__), "day2.txt")) as f:
    part1 = part2 = 0

    for line in f:
        low, high, c, word = re.findall("(\d+)-(\d+) (\w): (\w+)", line.strip())[0]
        low, high = int(low), int(high)

        if low <= Counter(word)[c] <= high:
            part1 += 1

        if (word[low-1] == c) ^ (word[high-1] == c):
            part2 += 1

    print("Part 1:", part1)
    print("Part 2:", part2)