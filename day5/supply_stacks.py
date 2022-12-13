def get_box_indices(stack_numbers, line):
        box_indices = []
        for stack_number in stack_numbers:
            box_indices.append(line.index(stack_number))
        return box_indices

def get_stacks(input, box_indices):
        rows = [a for a in range(len(box_indices))]
        rows_reversed = rows[::-1]
        stacks = [list() for _ in range(len(box_indices))]
        for index in rows_reversed:
            line = input[index]
            for i in range(len(box_indices)):
                if (line[box_indices[i]] != " "):
                    stacks[i].append(line[box_indices[i]])
        return stacks

def make_stacks(input, empty_line_index):
    stack_numbers = re.findall("\d+", input[empty_line_index - 1])
    box_indices = get_box_indices(stack_numbers, input[empty_line_index - 1])
    stacks = get_stacks(input, box_indices)
    return stacks

def operate_crane(input, stacks):
    for line in input:
        parsed = re.findall("\d+", line)
        num_to_move = int(parsed[0])
        source = int(parsed[1]) - 1
        dest = int(parsed[2]) - 1
        for _ in range(num_to_move):
            box = stacks[source].pop()
            stacks[dest].append(box)
    return

def operate_crane_2(input, stacks):
    for line in input:
        parsed = re.findall("\d+", line)
        num_to_move = int(parsed[0])
        source = int(parsed[1]) - 1
        dest = int(parsed[2]) - 1
        staging_area = []
        for _ in range(num_to_move):
            box = stacks[source].pop()
            staging_area.append(box)
        for _ in range(num_to_move):
            stacks[dest].append(staging_area.pop())
    return

def get_top_crates(stacks):
    top_crates = []
    for stack in stacks:
        top_crates.append(stack.pop())
    return top_crates

def part2():
    with open(sys.argv[1]) as f:
        input = f.readlines()
        empty_line_index = input.index("\n")
    stacks = make_stacks(input, empty_line_index)
    operate_crane_2(input[empty_line_index + 1:], stacks)
    top_crates = get_top_crates(stacks)
    print("\nPart 2: Top of each stack -> "+str(top_crates))

def part1():
    with open(sys.argv[1]) as f:
        input = f.readlines()
        empty_line_index = input.index("\n")
    stacks = make_stacks(input, empty_line_index)
    operate_crane(input[empty_line_index + 1:], stacks)
    top_crates = get_top_crates(stacks)
    print("\nPart 1: Top of each stack -> "+str(top_crates))

import sys, re
if (len(sys.argv) != 2):
    sys.exit("\n[ERROR: Carmy] Input error!")

part1()
part2()