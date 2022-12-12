import queue
from collections import deque


def find_positions(grid, part_two):
    start_pos = (0, 0)
    end_pos = (0, 0)
    lowest = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start_pos = (row, col)
                grid[row][col] = 0
            elif grid[row][col] == 'E':
                end_pos = (row, col)
                grid[row][col] = 25
            elif grid[row][col] == 'a' and part_two:
                grid[row][col] = ord(grid[row][col]) - ord('a')
                lowest.append((row, col))
            else:
                grid[row][col] = ord(grid[row][col]) - ord('a')
    return start_pos, end_pos, lowest


def bfs(grid, start_pos, end_pos):
    q = deque()
    explored = set([start_pos])
    q.append((0, start_pos))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        steps, pos = q.popleft()
        if pos == end_pos:
            return steps

        x, y = pos
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) \
                and grid[new_x][new_y] <= grid[x][y] + 1 \
                and (new_x, new_y) not in explored:
                    explored.add((new_x, new_y))
                    q.append((steps + 1, (new_x, new_y)))
    return -1


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    grid = [list(ln) for ln in lines]
    start_pos, end_pos, lowest = find_positions(grid, True)
    lowest.append(start_pos)

    steps = []
    for start in lowest:
        x = bfs(grid, start, end_pos)
        if x != -1:
            steps.append(x)


    print(bfs(grid, start_pos, end_pos)) # first part solution
    print(min(steps)) # second part solution
