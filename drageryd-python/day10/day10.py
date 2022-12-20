import sys

data = sys.stdin.read().strip()


codes = [tuple(c.split(" ")) for c in data.split("\n")]

# Single register
X = 1
t = 1

def noop(args):
    pass

def addx(args):
    global X
    X += int(args[0])

# Instructions can modify the global variable X
# And adjust the clock t with the number of cycles spent
instructions = {
    "noop": (noop, 1),
    "addx": (addx, 2),
}

strengths = 0
image = []
next_iteration = 20
for code in codes:
    # Break the line into instruction and arguments
    instruction, cycles = instructions[code[0]]
    args = code[1:]
    for c in range(cycles):
        # Always draw to image
        if X - 1 <= len(image) % 40 <= X + 1:
            image.append("#")
        else:
            image.append(".")

        t += 1
        # Perform instruction at last cycle
        if c == cycles - 1:
            instruction(args)
        # Add strengths to sum
        if t >= next_iteration:
            #print("t={} X={}".format(t, X))
            strengths += t * X
            next_iteration += 40
# Build final CRT image
image = "".join(c + "\n" if i % 40 == 39 else c for i,c in enumerate(image))

print("Part 1: {}".format(strengths))
print("Part 2: \n{}".format(image))
