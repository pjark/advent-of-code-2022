import sys

if len(sys.argv) != 2:
    sys.exit("[ERROR: Carmy] Input error!")

num_elves = 1
calories = []
num_calories = 0

with open(sys.argv[1]) as f:
    for line in f:
        if line == "\n":
            num_elves += 1
            calories.append(num_calories)
            num_calories = 0
        else:
            num_calories += int(line)
    calories.append(num_calories)

print("\nElf with the most calories:")
print("elf "+str(calories.index(max(calories)))+" with "+str(max(calories))+" calories")

top_three = []
for _ in range(3):
    max_val = max(calories)
    top_three.append(max_val)
    calories.remove(max_val)

print("\nTop Three numbers of calories: "+str(top_three))
print("sum of top three: "+str(sum(top_three)))
