import sys
from itertools import permutations

data = sys.stdin.read().strip()
data2 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

# Generate a list of sets for each elfs ranges
sections = [
    [
        frozenset(range(
            int(r.split("-")[0]),
            int(r.split("-")[1]) + 1
        ))
        for r in line.split(",")
    ]
    for line in data.split("\n")
]

# Count how many ranges are contained inside another
inside = 0
for elf in sections:
    for a,b in permutations(elf, 2):
        if a.intersection(b) == a:
            inside += 1
            #print("{}-{} fully contains {}-{}".format(
            #    min(b), max(b),
            #    min(a), max(a)))
            # Break if the two elves got the same range it wount be counted twice
            break
print("Part 1: {}".format(inside))

# Count how many ranges overlap
overlap = 0
for a, b in sections:
    if a.intersection(b):
        overlap += 1
        #print("{}-{},{}-{} overlaps in sections {}-{}".format(
        #    min(b), max(b),
        #    min(a), max(a),
        #    min(a.intersection(b)), max(a.intersection(b))))
print("Part 2: {}".format(overlap))
