def clear(speed=1.5):
    time.sleep(speed)
    os.system( 'clear' )

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
        
def do_actions_too(input, speed=None):
    def get_actions_from_input(input):
        actions = []
        for move, steps in input:
            for _ in range(int(steps)):
                actions.append(move)
        return actions

    def print_map(actions, head=None, knots=None, move=None, index=None):
        ### handle defaults
        if not head or not knots: 
            print("\nBtw, head and knots are set to their defaults")
            head = [0,0]
            knots = [[0,0] for _ in range(9)]

        ### get the bounds
        bounds_dict = { 'R':0, 'L':0, 'U':0, 'D':0 }
        for action in actions: bounds_dict[action] += 1
        occurences = [bounds_dict[key] for key in bounds_dict]
        map_bounds = max(occurences) * 2 + 1; # print("bounds for map =", map_bounds)
        add = max(occurences)

        temp_actions = [action for action in actions]
        if index: temp_actions[index] += "*"
        print(' '.join(temp_actions))
        
        ### get the map 
        the_map = [[] for _ in range(map_bounds)]
        for index in range(map_bounds): the_map[index] = ['.' for _ in range(map_bounds)]
        # fill knots, start, and head
        the_map[0+add][-(0+add)] = 's'
        last = None
        for index, knot in enumerate(knots):
            if last != knot:
                the_map[knot[0]+add][-(knot[1]+add)] = str(index+1)
            last = knot
        the_map[head[0]+add][-(head[1]+add)] = 'H'
        
        ### print the map
        # for x in range(map_bounds): print(''.join(the_map[x]))
        for x in range(map_bounds):
            for y in range(map_bounds):
                print(the_map[y][x], end='')
            print('')

    def move_head(prev_head, action):
        if action not in ['R', 'L', 'U', 'D']: sys.exit("\n[ERROR: John] Invalid action!")
        if action == 'R':   new_head = [prev_head[0]+1, prev_head[1]]
        elif action == 'L': new_head = [prev_head[0]-1, prev_head[1]]
        elif action == 'U': new_head = [prev_head[0], prev_head[1]+1]
        elif action == 'D': new_head = [prev_head[0], prev_head[1]-1]
        return new_head

    def move_knot(leader, follower):
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

        if leader == follower or adjacent(leader, follower): # don't move
            return follower
        elif leader[0] == follower[0] or leader[1] == follower[1]: # cardinal move
            if leader[0] == follower[0]:
                possible_new_locs = [
                    [follower[0], follower[1]+1],
                    [follower[0], follower[1]-1]
                ]
                for possible_new_loc in possible_new_locs:
                    if adjacent(leader, possible_new_loc):
                        return possible_new_loc
            elif leader[1] == follower[1]:
                possible_new_locs = [
                    [follower[0]+1, follower[1]],
                    [follower[0]-1, follower[1]]
                ]
                for possible_new_loc in possible_new_locs:
                    if adjacent(leader, possible_new_loc):
                        return possible_new_loc
        elif math.dist(leader, follower) > 2.0: # diagonal move
            possible_new_locs = [
                [follower[0]-1, follower[1]-1],
                [follower[0]-1, follower[1]+1],
                [follower[0]+1, follower[1]-1],
                [follower[0]+1, follower[1]+1]
            ]
            for possible_new_loc in possible_new_locs:
                if adjacent(leader, possible_new_loc):
                    return possible_new_loc

        sys.exit("\n[ERROR: Harry] Adjacent point not found!\n")
    
    ### get actions and starting locations
    actions = get_actions_from_input(input); # print(actions)
    head = [0,0]; knots = [[0,0] for _ in range(9)]
    if speed: clear(0); print_map(actions, head, knots)

    ### move head and knots based on action
    ### track with visited
    visited = set()
    for index, action in enumerate(actions):
        head = move_head(head, action)
        for knot_index, knot in enumerate(knots):
            if knot_index == 0: leader = head
            else: leader = knots[knot_index-1]
            knots[knot_index] = move_knot(leader, knot)
            visited.add(tuple(knots[-1]))
        if speed: clear(speed); print_map(actions, head, knots, action, index)
        # if index == 22: break
        
    return visited
        
def part2(speed=None): # 9 knots (knot #9 = tail)
    input = get_formatted_input(sys.argv[1]); # [print(line) for line in input]
    visited = do_actions_too(input, speed); # print visited
    
    # sys.exit("\nPurposefully stopped.\n")
    print("\nPart 2: The tail knot visited", len(visited), "positions at least once.\n")

def part1(): # 1 knot (knot = tail)
    input = get_formatted_input(sys.argv[1]); # [print(line) for line in input]
    visited = do_actions(input); # print(visited)

    print("\nPart 1: The tail visited", len(visited), "positions at least once.")

import sys, math, os, time
if len(sys.argv) != 2:
    sys.exit("\n[ERROR: Carmy] Incorrect input arguments!")

part1()
part2(speed=0) # use 0 for no output