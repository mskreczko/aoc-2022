import math

def process_input(lines):
    starting_items = lines[1].split(', ')
    starting_items = [int(x.split(': ')[1]) if i == 0 else int(x) for i, x in enumerate(starting_items)]
    operation = lines[2].split(' = ')[1].split(' ')
    test = int(lines[3].split(' ')[-1])
    if_true = int(lines[4].split(' ')[-1])
    if_false = int(lines[5].split(' ')[-1])
    return {'items': starting_items, 'op': operation, 'test': test, 'true': if_true, 'false': if_false}


with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')
    monkeys_items = []
    init = [process_input(monkey.splitlines()) for monkey in data]
    inspected_items = [0 for _ in range(len(init))]
    mod = math.lcm(*[m['test'] for m in init])

    for _ in range(10000):
        print(_)
        for j, monkey in enumerate(init):
            to_delete = []
            for i, item in enumerate(monkey['items']):
                if monkey['op'][2] == 'old':
                    worry_level = eval(str(item) + monkey['op'][1] + str(item)) % mod # if part one then divide by 3
                else:
                    worry_level = eval(str(item) + monkey['op'][1] + monkey['op'][2]) % mod
                if worry_level % monkey['test'] == 0:
                    init[monkey['true']]['items'].append(worry_level)
                else:
                    init[monkey['false']]['items'].append(worry_level)
                to_delete.append(i)
                inspected_items[j] += 1
            monkey['items'] = [v for i, v in enumerate(monkey['items']) if i not in frozenset(to_delete)]

    most_active = sorted(inspected_items)[-2:]
    print(most_active[0] * most_active[1]) # solution
