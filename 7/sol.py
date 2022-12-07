with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

dirs = []
dirs_sizes = {}
for ln in lines:
    splitted = ln.split()
    if splitted[0] == '$':
        if splitted[1] == 'cd':
            dst = splitted[2]
            if dst == '..':
                dirs.pop()
            elif dst == '/':
                dirs = ['/']
            else:
                dirs.append(dst)
    else:
        if splitted[0] != 'dir':
            path = ""
            for d in dirs:
                if d != '/' and path != '/':
                    path += '/'
                path += d
                dirs_sizes[path] = dirs_sizes.get(path, 0) + int(splitted[0])

print(sum([v for n, v in dirs_sizes.items() if v < 100000])) # first part solution
print(min([v for n, v in dirs_sizes.items() if v >= 30000000 - (70000000 - dirs_sizes.get('/'))])) # second part solution
