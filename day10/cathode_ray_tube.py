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

def draw_render(draw):
    print('')
    newlines = [n for n in range(39, 240, 40)]
    for i in range((len(draw))):
        print(draw[i], end='')
        if i in newlines: print('')
    print('')

def render(queue):
    crt = 1
    crt_pos = update_crt(crt)

    pixels = ['.' for _ in range(240)]

    for pixel in range(240):
        if pixel in crt_pos: pixels[pixel] = '#'

        cycle = pixel + 1
        if cycle == queue[0][0]:
            crt += queue[0][1]
            crt_pos = update_crt(crt)
            queue.pop(0)

    draw_render(pixels)

def main():
    if len(sys.argv) != 2: sys.exit("\n[ERROR] Invalid input args!")

    ### Part 1
    input = get_input_from_file(sys.argv[1])
    signal_strengths, command_queue = cpu(input)
    # print("\nPart 1: Sum of signal strengths =", sum(signal_strengths))

    ### Part 2
    render(command_queue)

if __name__ == '__main__':
    main()