def parse_input(input):
    matches = re.findall("\d+", input)
    return [int(i) for i in matches]

def is_subset(a1, a2, b1, b2):
    a = set([i for i in range(a1, a2+1)])
    b = set([i for i in range(b1, b2+1)])
    if (a.issubset(b) or b.issubset(a)):
        return 1
    else: 
        return 0

def part1():
    with open(sys.argv[1]) as f:
        num_pairs = 0
        for line in f:
            a1, a2, b1, b2 = parse_input(line)
            num_pairs += is_subset(a1, a2, b1, b2)
    print("\nPart 1: "+str(num_pairs)+" assignment pairs")

def overlap(a1, a2, b1, b2):
    for num in range(a1, a2+1):
        if num in range(b1, b2+1):
            return 1
    return 0

def part2():
    with open(sys.argv[1]) as f:
        num_pairs = 0
        for line in f:
            a1, a2, b1, b2 = parse_input(line)
            num_pairs += overlap(a1, a2, b1, b2)
    print("\nPart 2: "+str(num_pairs)+" assignment pairs overlap")

import sys, re 
if (len(sys.argv) != 2):
    sys.exit("\n[ERROR: Carmy] Input error!")

part1()
part2()