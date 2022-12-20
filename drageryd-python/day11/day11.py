import sys
import math

data = sys.stdin.read().strip()

# Parse input
def parse(data):
    def monkey_number(l):
        # "Monkey X:" -> return X
        return int(l.split(" ")[1][:-1])
    def monkey_items(l):
        # "  Starting items: X, Y, Z" -> Return [X, Y, Z]
        return list(map(int, l.split(": ")[1].split(", ")))
    def monkey_operation(l):
        # "  Operation: new = old + 5" -> Return "new = old + 5"
        # This is just a string that will be evaluated later using eval()
        return l.split(" = ")[1]
    def monkey_test(l):
        # "  Test: divisible by X" -> return X
        return int(l.split("by ")[1])
    def monkey_throw(l):
        # "    If true/false: throw to monkey X" -> Return X
        return int(l.split("monkey ")[1])
    # Parsers per index in input
    p = [monkey_number, monkey_items, monkey_operation, monkey_test, monkey_throw, monkey_throw]

    # Split by monkey and parse every monkey row
    # Add inspection count at the end
    return [[p[i](l)
             for i,l
             in enumerate(line.split("\n"))] + [0]
            for line
            in data.split("\n\n")]

# Evaluate operation
# Uses "old" as a keyword
def inspect_operation(old, operation):
    return eval(operation)

# Do one round for every monkey
def round(monkeys, part1):
    # Calculate product of all monkey divisors
    pd = math.prod(m[3] for m in monkeys)
    for monkey, items, operation, test, test_true, test_false, count in monkeys:
        # Inspect all items
        while items:
            # Get items in order
            i = items.pop(0)
            # Inspect operation
            i = inspect_operation(i, operation)
            if part1:
                # Divide by 3 after inspection
                i = i // 3
            else:
                # Truncate number by product of all divisors
                # This keeps the numbers within reasonable limits without
                #  breaking the math between all monkey operations
                i = i % pd
            # Test worry level
            if i % test == 0:
                monkeys[test_true][1].append(i)
            else:
                monkeys[test_false][1].append(i)
            # Add inspection count
            monkeys[monkey][6] += 1

monkeys = parse(data)
for i in range(20):
    round(monkeys, True)
inspection_count = sorted([m[6] for m in monkeys], reverse=True)
print("Part 1: {}".format(inspection_count[0] * inspection_count[1]))

monkeys = parse(data)
for i in range(10000):
    round(monkeys, False)
inspection_count = sorted([m[6] for m in monkeys], reverse=True)
print("Part 2: {}".format(inspection_count[0] * inspection_count[1]))
