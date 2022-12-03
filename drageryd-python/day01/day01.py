import sys

data = sys.stdin.read().strip()

elves = [sum(map(int, line.split("\n"))) for line in data.split("\n\n")]

print("Part 1: {}".format(max(elves)))
print("Part 2: {}".format(sum(sorted(elves)[-3:])))
