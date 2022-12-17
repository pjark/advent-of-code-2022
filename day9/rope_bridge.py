def get_formatted_input(file):
    with open(file) as f:
        input = f.readlines()
    formatted_input = []
    for line in input:
        formatted_input.append(line.replace('\n', '').split(' '))
    return formatted_input

def print_map(head_loc, tail_loc, input):
    # calculate a consistent bounds
    bounds_dict = {
        'R':0,
        'L':0,
        'U':0,
        'D':0
    }
    for direction, steps in input:
        bounds_dict[direction] += int(steps)
    
    bounds_vals = []
    for key in bounds_dict:
        bounds_vals.append(bounds_dict[key])

    bounds = max(bounds_vals)

    map = [[] for _ in range(bounds*2)]
    for x in range(bounds*2):
        for _ in range(bounds*2):
            map[x].append(".")
    
    map[0+bounds][0+bounds] = 's'
    map[tail_loc[0]+bounds][tail_loc[1]+bounds] = 'T'
    map[head_loc[0]+bounds][head_loc[1]+bounds] = 'H'
    
    for line in map:
        print(''.join(line))
    
    return 

def do_actions(input):
    def move_head(head_loc, move):
        # R = (+1, 0), L = (-1, 0), U = (0, +1), D = (0, -1)
        if move == 'R':
            head_loc[1] += 1
        elif move == 'L':
            head_loc[1] -= 1
        elif move == 'U':
            head_loc[0] -= 1
        elif move == 'D':
            head_loc[0] += 1
        else:
            sys.exit("[ERROR: Veronica] Unknown move")

        return head_loc

    def adjacent(head_loc, tail_loc):
        # adjacent can be any position touching the head_loc
        if head_loc[0] == tail_loc[0]:
            if abs(head_loc[1] - tail_loc[1]) == 1:
                return True
        elif head_loc[1] == tail_loc[1]:
            if abs(head_loc[0] - tail_loc[0]) == 1:
                return True
        elif abs(head_loc[0] - tail_loc[0]) + abs(head_loc[1] - tail_loc[1]) == 2:
            return True
        else: return False

    def move_tail(head_loc, old_tail_loc, visited):
        if head_loc == old_tail_loc:
            return old_tail_loc

        new_tail_loc = -1
        if head_loc[0] == old_tail_loc[0] or head_loc[1] == old_tail_loc[1]:
            possible_new_locs = [
                [old_tail_loc[0]+1, old_tail_loc[1]],
                [old_tail_loc[0]-1, old_tail_loc[1]],
                [old_tail_loc[0], old_tail_loc[1]+1],
                [old_tail_loc[0], old_tail_loc[1]-1]
            ]
            for possible_new_loc in possible_new_locs:
                if adjacent(head_loc, possible_new_loc):
                    new_tail_loc = possible_new_loc
        elif math.dist(head_loc, old_tail_loc) > 2.0:
            possible_new_locs = [
                [old_tail_loc[0]-1, old_tail_loc[1]-1],
                [old_tail_loc[0]-1, old_tail_loc[1]+1],
                [old_tail_loc[0]+1, old_tail_loc[1]-1],
                [old_tail_loc[0]+1, old_tail_loc[1]+1]
            ]
            for possible_new_loc in possible_new_locs:
                if adjacent(head_loc, possible_new_loc):
                    new_tail_loc = possible_new_loc

        # sanity checking
        if new_tail_loc == -1:
            print("\n[Error: Martha] Adjacent position somehow not found!")
            print("-> head @", head_loc, "& tail @", old_tail_loc)
            print("-> map:"); print_map(head_loc, tail_loc)
            sys.exit("\n")
        if not adjacent(head_loc, new_tail_loc):
            print("\n[Error: Steve] Tail was not correctly moved!")
            print("\thead @", head_loc)
            print("\ttail moved from", tail_loc, "to", new_tail_loc)
            sys.exit("\n")
        else:
            visited.add(tuple(new_tail_loc))
            return new_tail_loc

    visited = set(); visited.add(tuple([0,0]))
    head_loc = [0,0]
    tail_loc = [0,0]
    for line in input:
        direction, steps = line
        movement_queue = [direction for _ in range(int(steps))]
        # print("\n=======", direction, steps, "========", end='')
        for move in movement_queue:
            head_loc = move_head(head_loc, move)
            if not adjacent(head_loc, tail_loc):
                tail_loc = move_tail(head_loc, tail_loc, visited)
            # print(''); print_map(head_loc, tail_loc, input)
    return visited
        
def part1():
    input = get_formatted_input(sys.argv[1]); # [print(line) for line in input]
    visited = do_actions(input); # print(visited)
    print("\nPart 1: The tail visited", len(visited), "positions at least once.\n")

import sys, math
if len(sys.argv) != 2:
    sys.exit("[ERROR: Carmy] Incorrect input arguments!")

part1()