import sys

data = sys.stdin.read().strip()

# Generate a grid of trees and assume that no trees are visible
grid = {(x,y): int(c)
        for y,row in enumerate(data.split("\n"))
        for x,c in enumerate(row)}

size_x = max(x for x,y in grid)
size_y = max(y for x,y in grid)

# Keep track of visible trees
visible = set()

# Generator for a tuple range from start along one axis
# Note: start is not included in the range, it can be considered
#  the coordinate from which the viewer "looks" e.g outside the grid
# Note: This can miss the end and loop infinitely if the end
#  is not in-line with start along the step axis
def coordinate_range(start, step, end):
    coord = start
    while coord[0] != end[0] or coord[1] != end[1]:
        coord = tuple(map(sum, zip(coord, step)))
        yield coord

# Check along a line of coordinates which coordinates are visible
def find_visible(grid, coordinates):
    visible = set()
    current_height = -1
    for x, y in coordinates:
        if current_height == 9:
            break
        elif grid[(x,y)] > current_height:
            visible.add((x,y))
            current_height = grid[(x,y)]
    return visible

# Check all rows and columns from edges of grid
visible = set()
for row in range(size_y + 1):
    visible |= find_visible(grid, coordinate_range((-1,row), (1,0), (size_x,row)))
    visible |= find_visible(grid, coordinate_range((size_x+1,row), (-1,0), (0,row)))
for col in range(size_x + 1):
    visible |= find_visible(grid, coordinate_range((col,-1), (0,1), (col,size_y)))
    visible |= find_visible(grid, coordinate_range((col,size_y+1), (0,-1), (col,0)))
print("Part 1: {}".format(len(visible)))

# See how long the view is from a tree
def viewing_distance(grid, tree, coordinates):
    distance = 0
    for c in coordinates:
        distance += 1
        if grid[c] >= grid[tree]:
            break
    return distance

# Find the best coordinate
best_scenic_score = -1
for x,y in grid:
    # Look in all directions and count how many trees are visible
    right = viewing_distance(grid, (x,y), coordinate_range((x,y), (1,0), (size_x,y)))
    left = viewing_distance(grid, (x,y), coordinate_range((x,y), (-1,0), (0,y)))
    down = viewing_distance(grid, (x,y), coordinate_range((x,y), (0,1), (x,size_y)))
    up = viewing_distance(grid, (x,y), coordinate_range((x,y), (0,-1), (x,0)))
    scenic_score = right * left * down * up
    #print("{}: {} * {} * {} * {} = {}".format((x, y), right, left, down, up, scenic_score))
    best_scenic_score = max(scenic_score, best_scenic_score)
print("Part 2: {}".format(best_scenic_score))
