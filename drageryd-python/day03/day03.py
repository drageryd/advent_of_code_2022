import sys
import string
from itertools import combinations

data = sys.stdin.read().strip()

# Split rucksack contents into compartments
rucksacks_compartments = [(frozenset(list(line[:len(line)//2])),
                           frozenset(list(line[len(line)//2:])))
                          for line in data.split("\n")]
# The compartments should contain unique items
common_items = [list(a.intersection(b)).pop() for a, b in rucksacks_compartments]

# Calculate priorities for duplicate items in bags
alphabet = string.ascii_letters
print("Part 1: {}".format(sum(alphabet.index(c) + 1 for c in common_items)))

# Create a list of the common items for every group of three
rucksacks = [frozenset(list(line)) for line in data.split("\n")]
group_badges = [list(frozenset.intersection(*triple))[0]
                for triple in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])]
print("Part 2: {}".format(sum(alphabet.index(c) + 1 for c in group_badges)))
