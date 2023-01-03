
class Monkey:
    def __init__(self, items, operation, operator, divisor, true_monkey, false_monkey):
        self.items = items
        self.true = true_monkey
        self.false = false_monkey
        self.operation = operation
        self.operator = operator
        self.divisor = divisor
    
    def operate(self, item):
        if self.operation == 'a':
            return item + self.operator
        elif self.operation == 'm':
            return item * self.operator
    
    def test(self, item):
        if item % self.operator == 0: return True
        else: return False

def get_example_input():
    monkey0 = Monkey([79, 98], 'm', 19, 23, 2, 3)
    monkey1 = Monkey([54, 65, 75, 74], 'a', 6, 19, 2, 0)
    monkey2 = Monkey([79, 60, 97], 'm', None, 13, 1, 3)
    monkey3 = Monkey([74], 'a', 3, 17, 0, 1)
    return monkey0, monkey1, monkey2, monkey3

def get_actual_input():
    monkey0 = Monkey([57, 58], 'm', 19, 7, 2, 3)
    monkey1 = Monkey([66, 52, 59, 79, 94, 73], 'a', 1, 19, 4, 6)
    monkey2 = Monkey([80], 'a', 6, 5, 7, 5)
    monkey3 = Monkey([82, 81, 68, 66, 71, 83, 75, 97], 'a', 5, 11, 5, 2)
    monkey4 = Monkey([55, 52, 67, 70, 69, 94, 90], 'm', None, 17, 0, 3)
    monkey5 = Monkey([69, 85, 89, 91], 'a', 7, 13, 1, 7)
    monkey6 = Monkey([75, 53, 73, 52, 75], 'm', 7, 2, 0, 4)
    monkey7 = Monkey([94, 60, 79], 'a', 2, 3, 1, 6)
    return monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7

def print_monkeys(monkey_list):
# Monkey 0:
#   Starting items: 57, 58
#   Operation: new = old * 19
#   Test: divisible by 7
#     If true: throw to monkey 2
#     If false: throw to monkey 3
    for index, monkey in enumerate(monkey_list):
        print("")
        print("Monkey "+str(index)+":")
        print("  Starting items: ", end=''); print(*monkey.items, sep=', ')
        if monkey.operation == 'a':
            if monkey.operator is None: print("  Operation: new = old + old")
            else: print("  Operation: new = old + ", monkey.operator)
        elif monkey.operation == 'm':
            if monkey.operator is None: print("  Operation: new = old * old")
            else: print("  Operation: new = old * ", monkey.operator)
        print("  Test: divisible by", monkey.divisor)
        print("    If true: throw to monkey", monkey.true)
        print("    If false: throw to monkey", monkey.false)
    print("")

def get_num_inspections(monkeys):
    def operate(old, operation, operator):
        if operation == 'a':
            if operator is None: return old + old
            else: return old + operator
        elif operation == 'm':
            if operator is None: return old * old
            else: return old * operator

    def print_inventory(monkeys):
        for index, monkey in enumerate(monkeys):
            print("Monkey "+str(index)+": ", end='')
            print(*monkey.items, sep=', ')

    num_inspections = [0 for _ in range(len(monkeys))]
    num_rounds = 20
    for _ in range(num_rounds):
        for index in range(len(monkeys)):
            current_monkey = monkeys[index]
            if current_monkey.items:
                for item in current_monkey.items:
                    num_inspections[index] += 1
                    new = operate(item, current_monkey.operation, current_monkey.operator)
                    new = int(new / 3)
                    if new % current_monkey.divisor == 0: monkeys[current_monkey.true].items.append(new)
                    else: monkeys[current_monkey.false].items.append(new)
                current_monkey.items = list()
    return num_inspections

def calc_monkey_business_level(num_inspections):
    num_inspections.sort(); # print(num_inspections)
    top_two = num_inspections[-2:]; # print(top_two)
    return top_two[0] * top_two[1]

def main():
    monkeys = get_example_input() # 0-3
    # monkeys = get_actual_input() # 0-7
    num_inspections = get_num_inspections(monkeys)
    monkey_business_level = calc_monkey_business_level(num_inspections)
    print("\nPart 1: Level of monkey business =", monkey_business_level)

import sys
if __name__ == '__main__':
    main()