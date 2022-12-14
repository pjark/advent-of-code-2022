def get_input_from_file(file):
    with open(file) as f:
        return f.readlines()

def print_value_table(value_table):
    print("\nprinting forest...")
    for row in value_table:
        print(row)

def print_adj_list(adj_list):
    for key in adj_list:
        print(key, " -> ", adj_list[key])

def create_matrix(input):
    matrix = {} # create matrix
    value_table = [[] for _ in range(len(input))]
    for index, line in enumerate(input): # populate matrix
        matches = re.findall("\d", line)
        value_table[index] = matches
        for y_coord, value in enumerate(matches):
            coords = (index, y_coord)
            matrix[coords] = value
    return value_table, matrix

def create_adj_list(matrix, min_val, max_val):
    def get_all_adjacent(coord, min_val, max_val):
        all_adjacent = {}
        left = []; right = []; up = []; down = []
        # left
        curr = coord
        while True:
            test = (curr[0]-1, curr[1])
            if min_val in test or max_val in test:
                break
            left.append(test)
            curr = test
        # right
        curr = coord
        while True:
            test = (curr[0]+1, curr[1])
            if min_val in test or max_val in test:
                break
            right.append(test)
            curr = test
        # up 
        curr = coord
        while True:
            test = (curr[0], curr[1]-1)
            if min_val in test or max_val in test:
                break
            up.append(test)
            curr = test
        # down
        curr = coord
        while True:
            test = (curr[0], curr[1]+1)
            if min_val in test or max_val in test:
                break
            down.append(test)
            curr = test
        all_adjacent["left"] = left
        all_adjacent["right"] = right
        all_adjacent["up"] = up
        all_adjacent["down"] = down
        return all_adjacent
    adj_list = {}
    for coord in matrix:
        if min_val not in coord and max_val not in coord:
            all_adjacent_coords = get_all_adjacent(coord, min_val-1, max_val+1)
            adj_list[coord] = all_adjacent_coords
    return adj_list

def find_not_visible_trees(adj_list, value_dict):
    # trees visible from outside if all adjacent trees are smaller
    visible_from_direction = {}
    for tree in adj_list:
        visible_from_direction[tree] = {'left':1, 'right':1, 'up':1, 'down':1}
        directions = ['left', 'right', 'up', 'down']
        for direction in directions:
            for adj_tree in adj_list[tree][direction]:
                if value_dict[adj_tree] >= value_dict[tree]:
                    # tree not visible from this direction
                    visible_from_direction[tree][direction] = 0
    not_visible_trees = set()
    visible_inner_trees = set()
    for tree in visible_from_direction:
        visible = 0
        for direction in visible_from_direction[tree]:
            visible += visible_from_direction[tree][direction]
        if not visible:
            not_visible_trees.add(tree)
        else:
            visible_inner_trees.add(tree)
    return len(not_visible_trees)

def part1():
    input = get_input_from_file(sys.argv[1])
    value_table, matrix = create_matrix(input)
    adj_list = create_adj_list(matrix, 0, len(value_table[0])-1); # print_adj_list(adj_list)
    num_not_visible = find_not_visible_trees(adj_list, matrix); # print("\ntotal trees =", len(matrix.keys()), "\n# of trees not visible =", num_not_visible)
    print("\nPart 1: Number of visible trees visible from outside the grid =", len(matrix.keys()) - num_not_visible)

import sys, re
if len(sys.argv) != 2:
    sys.exit("[ERROR: Carmen] Invalid input arguments!")

part1()