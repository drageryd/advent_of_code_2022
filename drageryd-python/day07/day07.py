import sys

data = sys.stdin.read().strip()

# Ugly parse data into directory tree
def parse(data):
    root = {"type": "dir", "ls": {}}
    pwd = root
    for line in data.split("\n"):
        line = line.split(" ")
        if line[0] == "$":
            # Commands begin with dollar sign
            if line[1] == "cd":
                # cd command changes the current directory
                if line[2] == "/":
                    pwd = root
                elif line[2] == "..":
                    # Go to parent directory if existing
                    if "parent" in pwd:
                        pwd = pwd["parent"]
                else:
                    # Go to child directory from current
                    # Note: This will break if trying to navigate to file
                    pwd = pwd["ls"][line[2]]
            elif line[1] == "ls":
                # ls lists content but the line itself does not matter
                pass
        else:
            # Any other lines will be ls output in the current directory
            if line[0] == "dir":
                # directories will be populated in the tree
                # Note: Assuming all directories are visited exactly once
                pwd["ls"][line[1]] = {"type": "dir", "parent": pwd, "ls": {}}
            else:
                # Files start with their size listed
                pwd["ls"][line[1]] = {"type": "file", "size": int(line[0])}
    return root

# Pretty print any directory structure
def pprint(tree, name="/", indent=""):
    print("{}- {} ({}, size={})".format(indent,
                                        name,
                                        tree["type"],
                                        tree.get("size", "?")))
    if tree["type"] == "dir":
        for name, child_tree in tree["ls"].items():
            pprint(child_tree, name, indent + "  ")
        
# Recursively calculate size of directories
# Return a tuple of the size of the current tree/dir/file as well as
#  the sum of all the child directories that have a total size of at most "limit"
# While calculating the sizes, store them in an array for later use
def calc_size(tree, limit, all_dir_sizes):
    # If the item is a file return size
    if tree["type"] == "file":
        return (tree["size"], 0)
    # Else loop through the contents of directory and calculate size and sum
    dir_size = 0
    sum_limit = 0
    for name, child_tree in tree["ls"].items():
        ds, sl = calc_size(child_tree, limit, all_dir_sizes)
        dir_size += ds
        sum_limit += sl
    # If this directory is smaller than limit add it to sum_limit
    if dir_size <= limit:
        sum_limit += dir_size
    # Store directory size in size array
    all_dir_sizes.append(dir_size)
    return dir_size, sum_limit


tree = parse(data)
#pprint(tree)
all_dir_sizes = []
root_size, sum_limit = calc_size(tree, 100000, all_dir_sizes)
print("Part 1: {}".format(sum_limit))

# Disk information
total_disk_space = 70000000
needed_space = 30000000
current_space = total_disk_space - root_size
minimum_size_to_delete = needed_space - current_space

# Loop through the list of sizes and find the one that is closest
print("Part 2: {}".format(min(s for s in all_dir_sizes if s >= minimum_size_to_delete)))
