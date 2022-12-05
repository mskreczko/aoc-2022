with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    split_idx = next((i, l) for i, l in enumerate(lines) if 'move' in l)[0]
    instructions = lines[10:]

stacks = {
            '1': ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
            '2': ['L', 'D', 'Z', 'Q', 'W', 'V'],
            '3': ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
            '4': ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
            '5': ['Z', 'W', 'L', 'C'],
            '6': ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
            '7': ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
            '8': ['D', 'P', 'J'],
            '9': ['D', 'C', 'N', 'W', 'V']
        }

for instr in instructions:
    s = instr.split(' ')
    n = s[1]
    src = s[3]
    dst = s[5]
    for i in range(int(n)):
        x = stacks[src].pop()
        stacks[dst].append(x)

print(''.join([stacks[s].pop() for s in stacks])) # first part solution

# stacks = {
#             '1': ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
#             '2': ['L', 'D', 'Z', 'Q', 'W', 'V'],
#             '3': ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
#             '4': ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
#             '5': ['Z', 'W', 'L', 'C'],
#             '6': ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
#             '7': ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
#             '8': ['D', 'P', 'J'],
#             '9': ['D', 'C', 'N', 'W', 'V']
#         }

for instr in instructions:
    s = instr.split(' ')
    n = int(s[1])
    src = s[3]
    dst = s[5]
    stacks[dst] += stacks[src][n * -1:]
    del stacks[src][n * -1:]

for s in stacks.keys(): # second part solution
    print(stacks[s].pop(), end='')
