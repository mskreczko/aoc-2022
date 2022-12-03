import string

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    priorities_sum = 0
    for ln in lines:
        first_compartment, second_compartment = ln[:len(ln)//2], ln[len(ln)//2:]
        shared_item = set(first_compartment).intersection(set(second_compartment)).pop()
        priorities_sum += string.ascii_letters.find(shared_item) + 1
    print(priorities_sum) # first part solution
    
    priorities_sum = 0
    rucksacks_per_group = [lines[i:i+3] for i in range(0, len(lines), 3)]
    for rucksacks in rucksacks_per_group:
        shared_item = set(rucksacks[0]).intersection(rucksacks[1]).intersection(rucksacks[2]).pop()
        priorities_sum += string.ascii_letters.find(shared_item) + 1
    print(priorities_sum) # second part solution
