import sys

data = sys.stdin.read().strip()
# Process rounds to list of tuples
rounds = [tuple(line.split(" ")) for line in data.split("\n")]

# Look up tables for elf shape and the result based on my shape
# elf shape   - A: Rock, B: paper, C: scissors
# my shape    - X: Rock, Y: paper, Z: scissors
# round score - Win: 6, Draw: 3, Loss: 0
# shape score - Rock: 1, Paper: 2, Scissors: 3
def score(elf, me):
    round_lut = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }
    shape_lut = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return shape_lut[me] + round_lut[elf][me]

# Loop through and calculate score for each round
print("Part 1: {}".format(sum(score(elf, me) for elf, me in rounds)))

# Calculate shape to choose to get desired result
# elf shape - A: Rock, B: paper, C: scissors
# result    - X: Win, Y: Draw, Z: Loss
# return my hand to achieve result
def shape(elf, result):
    result_lut = {
        "A": {"X": "Z", "Y": "X", "Z": "Y"},
        "B": {"X": "X", "Y": "Y", "Z": "Z"},
        "C": {"X": "Y", "Y": "Z", "Z": "X"},
    }
    return result_lut[elf][result]

print("Part 2: {}".format(sum(score(elf, shape(elf, result)) for elf, result in rounds)))
