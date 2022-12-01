with open("data.txt") as f:
    data = f.read().split('\n')
    calories_per_elf = []
    curr_calories = 0
    for i in range(0, len(data)-1):
        if data[i] != '':
            curr_calories += int(data[i])
        else:
            calories_per_elf.append(curr_calories)
            curr_calories = 0

    print(max(calories_per_elf)) # first part solution
    print(sum(sorted(calories_per_elf)[-3:])) # second part solution
