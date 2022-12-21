import sys
from string import ascii_lowercase

data = sys.stdin.read().strip()

# Convert input to coordinate map with height information
#  and extract coordinates for start and end
def parse(data):
    hlut = {c: i for i,c in enumerate(ascii_lowercase)}
    hlut["S"] = hlut["a"]
    hlut["E"] = hlut["z"]
    start = 0
    end = 0
    hmap = {}
    for y, row in enumerate(data.split("\n")):
        for x, c in enumerate(row):
            coord = x + y*1j
            hmap[coord] = hlut[c]
            if c == "S":
                start = coord
            elif c == "E":
                end = coord
    return start, end, hmap
                
# Breadth first search from S to E in height map
def bfs(start, end, hmap, part1):
    queue = [(start,)]
    visited = set([start])
    steps = [1, -1, 1j, -1j]
    while queue:
        # Get next path from queue
        path = queue.pop(0)
        current_tile = path[-1]
        # If current tile is the finish tile we're done
        if part1:
            if current_tile == end:
                # Number of steps is one less than the number of tiles
                return len(path) - 1
        else:
            if hmap[current_tile] == 0:
                # Number of steps is one less than the number of tiles
                return len(path) - 1
            
        # Get possible coordinates to goto
        for s in steps:
            new_tile = current_tile + s
            # Only consider tiles in the grid
            if new_tile not in hmap:
                continue
            # Only continue if not already visited
            if new_tile in visited:
                continue
            # Check if step height is at most 1
            if part1:
                if hmap[new_tile] - hmap[current_tile] > 1:
                    continue
            else:
                # inverse the logic since we are searching in reverse
                if hmap[current_tile] - hmap[new_tile] > 1:
                    continue
            # Add to queue and visited
            queue.append(path + (new_tile,))
            visited.add(new_tile)

start, end, hmap = parse(data)
print("Part 1: {}".format(bfs(start, end, hmap, True)))
print("Part 1: {}".format(bfs(end, None, hmap, False)))
