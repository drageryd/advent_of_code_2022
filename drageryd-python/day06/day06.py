import sys

data = sys.stdin.read().strip()

# Find n unique characters in sequence
# Assuming the sequence exists
def detect(d, n):
    for i, c in enumerate(d):
        if len(set(d[i:i+n])) < n:
            continue
        else:
            return i + n
    
print("Part 1: {}".format(detect(data, 4)))
print("Part 2: {}".format(detect(data, 14)))
