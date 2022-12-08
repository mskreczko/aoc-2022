with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    grid = []
    for ln in lines:
        grid.append([int(x) for x in ln])

    visible_trees = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            curr_tree_height = grid[row][col]
            left_not = False
            right_not = False
            up_not = False
            bottom_not = False

            for x in range(col):
                if grid[row][x] >= curr_tree_height:
                    left_not = True
                    break

            for x in range(col + 1, len(grid[row])):
                if grid[row][x] >= curr_tree_height:
                    right_not = True
                    break

            for x in range(row):
                if grid[x][col] >= curr_tree_height:
                    up_not = True
                    break
            for x in range(row + 1, len(grid)):
                if grid[x][col] >= curr_tree_height:
                    bottom_not = True
                    break

            if False in [left_not, right_not, up_not, bottom_not]:
                visible_trees += 1

    print(visible_trees) # first part solution

    best_scenic_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            curr_tree_height = grid[row][col]
            L = R = U = D = 0
            for x in range(col - 1, -1, -1):
                L += 1
                if grid[row][x] >= curr_tree_height:
                    break

            for x in range(col + 1, len(grid[row])):
                R += 1
                if grid[row][x] >= curr_tree_height:
                        break

            for x in range(row - 1, -1, -1):
                U += 1
                if grid[x][col] >= curr_tree_height:
                    break
            
            for x in range(row + 1, len(grid)):
                D += 1
                if grid[x][col] >= curr_tree_height:
                    break
            best_scenic_score = max(best_scenic_score, L * R * U * D)

    print(best_scenic_score) # second part solution
