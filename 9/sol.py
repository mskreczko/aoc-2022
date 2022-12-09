with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = [ln.strip() for ln in lines]


dr = {'R': 1, 'L': -1, 'D': -1j, 'U': 1j}

def update_pos(h, t):
    diff = h - t
    if abs(diff.real) <= 1 and abs(diff.imag) <= 1:
        return 0
    dx = diff.real / abs(diff.real) if diff.real != 0 else 0
    dy = diff.imag / abs(diff.imag) if diff.imag != 0 else 0
    return dx + dy * 1j

def solve(knots):
    visited = set()
    positions = [0 for _ in range(knots)]
    for ln in lines:
        direction, steps = ln[0], int(ln[1:])
        for _ in range(steps):
            positions[0] += dr[direction]
            for i in range(1, knots):
                positions[i] += update_pos(positions[i-1], positions[i])
            visited.add(positions[-1])
    return len(visited)

print(solve(2)) # first part solution
print(solve(10)) # second part solution

