import sys

data = sys.stdin.read().strip()

def parse_moves(data):
    directions = {"R": 1, "L": -1, "U": 1j, "D": -1j}
    def parse(d, n):
        return directions[d], int(n)
    return [parse(*m.split(" ")) for m in data.split("\n")]

moves = parse_moves(data)

def tail_follow(head_position, tail_position, step):
    distance = head_position - tail_position
    if abs(distance.real) > 1 or abs(distance.imag) > 1:
        move_real = distance.real // abs(distance.real) if distance.real != 0 else 0
        move_imag = distance.imag // abs(distance.imag) if distance.imag != 0 else 0
        tail_position += move_real + move_imag * 1j
    return tail_position

# Move head along moves and let tail follow for a generic rope
def move_rope(moves, rope_length):
    rope = [0j for i in range(rope_length)]
    visited = set()
    # For every head move
    for step, steps in moves:
        # Repeat move n times
        for n in range(steps):
            # Move the head and let every tail follow
            rope[0] += step
            for i in range(1, rope_length):
                rope[i] = tail_follow(rope[i-1], rope[i], step)
            #print(rope)
            visited.add(rope[-1])
    return len(visited)

print("Part 1: {}".format(move_rope(moves, 2)))
print("Part 2: {}".format(move_rope(moves, 10)))
