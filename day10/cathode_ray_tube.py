import sys

def get_input_from_file(file):
    with open(file) as f:
        input = f.readlines()
    formatted_input = [line.replace('\n', '') for line in input]
    return formatted_input

def cpu(input):
    clock = 1
    queue = [] # clock num, value
    second_queue = []
    
    ### fill in command queue
    for line in input:
        if 'add' in line: 
            addx_str, value = line.split() # addx
            queue.append([clock+1, int(value)])
            second_queue.append([clock+1, int(value)])
            clock += 1
        else: 
            queue.append([clock, 0])
            second_queue.append([clock+1, 0])
        clock += 1

    ### run through command queue
    clock = 0
    reg = 1
    measure_cycle = [20, 60, 100, 140, 180, 220]
    measure_cycle_vals = []
    while True:
        clock += 1
        if clock in measure_cycle: 
            # print("clock:", clock, "   reg:", reg, "MEASURED")
            measure_cycle_vals.append(clock*reg)
        if clock == queue[0][0]:
            reg += queue[0][1]
            queue.pop(0)
        else: pass; # print("clock:", clock, "   reg:", reg)
        if not queue: break
    
    return measure_cycle_vals, second_queue

def update_crt(crt): return [crt-1, crt, crt+1]

def draw_render(row):
    print('')
    for i in range((len(row))):
        print(row[i], end='')
    print('')

def render(queue):
    # crt = 40 positions, 6 rows
    row = 0
    sprite_middle = 1
    sprite_pos = [sprite_middle-1, sprite_middle, sprite_middle+1]
    newlines = [n for n in range(40, 241, 40)]
    rows = [[] for n in range(6)]
    pixels = ['.' for _ in range(40)]

    for cycle in range(1, 241):
        position = cycle - (40 * row) - 1

        if (cycle - 1) == queue[0][0]:
            sprite_middle += queue[0][1]
            queue.pop(0)
            sprite_pos = [sprite_middle-1, sprite_middle, sprite_middle+1]

        if position in sprite_pos: pixels[position] = '#'

        if cycle in newlines:
            rows[row] = pixels 
            row += 1
            pixels = ['.' for _ in range(40)]

    print(''); [print(''.join(r)) for r in rows]; print('')

def main():
    if len(sys.argv) != 2: sys.exit("\n[ERROR] Invalid input args!")

    ### Part 1
    input = get_input_from_file(sys.argv[1])
    signal_strengths, command_queue = cpu(input)
    print("\nPart 1: Sum of signal strengths =", sum(signal_strengths), "\n")

    ### Part 2
    print("Part 2: \nThe capital letters will be displayed below:", end=''); render(command_queue)

if __name__ == '__main__':
    main()