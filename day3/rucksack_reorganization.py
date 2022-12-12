def get_compartments(rucksack):
    left = slice(0, len(rucksack) // 2)
    right = slice(len(rucksack) // 2, len(rucksack))
    return (rucksack[left], rucksack[right])

def find_duplicate(left, right):
    for letter in left:
        for other_letter in right:
            if (letter == other_letter):
                return letter
    return -1

def get_priority(letter):
    letter_ascii = ord(letter)
    if (letter_ascii in range(65, 90+1)): # uppercase
        return (letter_ascii - 38)
    elif (letter_ascii in range(97, 122+1)): # lowercase
        return (letter_ascii - 96)
    return -1

def part1():
    with open(sys.argv[1]) as f:
        total_score = 0
        for rucksack in f:
            left, right = get_compartments(rucksack)
            duplicate = find_duplicate(left, right)
            priority = get_priority(duplicate)
            if (priority not in range(1, 52+1)):
                sys.exit("\n[ERROR: Heather] Invalid priority for letter = "+str(duplicate))
            total_score += priority
            #print("duplicate: "+str(duplicate)+" priority: "+str(priority))
        print("\nPart 1 sum of priorities of duplicates: "+str(total_score))
    return 0

def find_common(group):
    # lmao this is very naive
    ruck1, ruck2, ruck3 = group
    for letter1 in ruck1:
        for letter2 in ruck2:
            if (letter1 == letter2):
                for letter3 in ruck3:
                    if (letter2 == letter3):
                        return letter3
    return 0

def part2():
    with open(sys.argv[1]) as f:
        rucksack_list = f.readlines()
        index = 0
        total_priority = 0
        while (index < len(rucksack_list)):
            group = [rucksack_list[index], rucksack_list[index+1], rucksack_list[index+2]]
            index += 3
            common = find_common(group)
            priority = get_priority(common)
            total_priority += priority
    print("\nPart 2 sum of priorities of commons: "+str(total_priority))

import sys 
if (len(sys.argv) != 2):
    sys.exit("\n[ERROR: Carmy] Input error!")

part1()
part2()