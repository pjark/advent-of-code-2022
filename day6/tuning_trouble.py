def create_initial_queue(input):
    window = []
    [window.append(input[i]) for i in range(4)]
    return window

def is_marker(window):
    for letter in window:
        if window.count(letter) > 1:
            return False
    return True

def move_window(window, input, index):
    window.pop(0)
    window.append(input[index])
    return window

def part1():
    with open(sys.argv[1]) as f:
        for line in f:
            window = create_initial_queue(line)
            index = 4
            while not is_marker(window):
                window = move_window(window, line, index)
                index += 1
            print("Part 1: "+str(index)+" characters processed before start-of-packet marker detected")

def create_initial_queue_message(input):
    window = []
    [window.append(input[i]) for i in range(14)]
    return window

def part2():
    with open(sys.argv[1]) as f:
        for line in f:
            window = create_initial_queue_message(line)
            index = 14
            while not is_marker(window):
                window = move_window(window, line, index)
                index += 1
            print("Part 2: "+str(index)+" characters processed before start-of-message marker detected")

import sys
if (len(sys.argv) != 2):
    sys.exit("\n[ERROR: Carmen] Something's up with the number of inputs!")

print("")
part1()
print("")
part2()
