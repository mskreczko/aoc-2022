with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    contained_ranges = 0
    overlapping_ranges = 0
    for ln in lines:
        first_range = [int(x) for x in ln.split(',')[0].split('-')]
        second_range = [int(x) for x in ln.split(',')[1].split('-')]

        if (first_range[0] >= second_range[0]) and (first_range[1] <= second_range[1]):
            contained_ranges += 1
        elif (first_range[0] <= second_range[0]) and (first_range[1] >= second_range[1]):
            contained_ranges += 1
        if (second_range[0] <= first_range[1]) and (second_range[1] >= first_range[1]):
            overlapping_ranges += 1
        elif (first_range[0] <= second_range[1]) and (first_range[1] >= second_range[1]):
            overlapping_ranges += 1

    print(contained_ranges) # first part solution
    print(overlapping_ranges) # second part solution
