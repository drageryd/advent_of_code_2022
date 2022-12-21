import sys
import functools

data = sys.stdin.read().strip()

def parse(data):
    return [[eval(l)
             for l in pair.split("\n")]
            for pair in data.split("\n\n")]

# Comparison returns -1 if in right order
def compare(a, b):
    #print("Comparing: {} vs {}".format(a, b))
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])
    else:
        # Both are list, iterate through elements
        for i in range(min(len(a), len(b))):
            c = compare(a[i], b[i])
            if c == 0:
                continue
            else:
                return c
        # If one list is longer than the other
        if len(a) < len(b):
            return -1
        elif len(a) == len(b):
            return 0
        else:
            return 1

packets = parse(data)
# Compare pairs of packets
s = 0
for i, pair in enumerate(packets):
    a, b = pair
    if compare(a, b) == -1:
        s += i + 1
print("Part 1: {}".format(s))f
        
# Flatten list to disregard pairs
packets = [p for pairs in packets for p in pairs]
# Add divider packets
d1 = [[2]]
d2 = [[6]]
packets.append(d1)
packets.append(d2)
# Sort using compare function
packets.sort(key=functools.cmp_to_key(compare))

# Find dividers again
print("Part 2: {}".format((packets.index(d1) + 1) * (packets.index(d2) + 1)))
