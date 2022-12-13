import sys
import re

data = sys.stdin.read().rstrip()
data2= """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

# Split stacks from moves
stacks_string, moves_string = data.split("\n\n")

# Parse stacks into a dictionary of lists populated bottom first
def parse_stacks(stack_string):
    stacks = []
    rows = stack_string.split("\n")
    # Add all stacks by column index except the last row (which contains labels)
    for row in rows[:-1]:
        # Digest line where one stack consumes 4 characters
        for i in range(len(row)//4+1):
            if i >= len(stacks):
                stacks.append([])
            # Get column string
            column = row[4*i:4*i+4]
            # If the column contains a stack add it to the corresponding stack
            m = re.search("(?<=\[)[A-Z](?=\])", column)
            if m:
                # Insert item first in list to keep top element last
                # this is slow now but should be faster later when moving around
                stacks[i].insert(0, m.group(0))
            #re.findall("((\d)+ ([a-z ]+) bag[s]*)+", rule)
    return stacks

# Parse moves "move X from Y to Z"
# into three values (X, Y, Z)
def parse_moves(moves_string):
    moves = []
    for line in moves_string.split("\n"):
        moves.append(tuple(map(int, re.findall("[0-9]+", line))))
    return moves

# Parse stacks and moves
stacks = parse_stacks(stacks_string)
moves = parse_moves(moves_string)

# Execute moves once for part 1
for n, f, t in moves:
    for i in range(n):
        # "from" and "to" are indexed from 1
        stacks[t-1].append(stacks[f-1].pop())

print("Part 1: {}".format("".join(s[-1] for s in stacks)))

# Reset stacks for part 2
stacks = parse_stacks(stacks_string)

# Execute moves once for part 2
for n, f, t in moves:
    t_end = len(stacks[t-1])
    for i in range(n):
        # "from" and "to" are indexed from 1
        stacks[t-1].insert(t_end, stacks[f-1].pop())

print("Part 12 {}".format("".join(s[-1] for s in stacks)))
