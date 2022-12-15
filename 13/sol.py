import functools
from math import prod


def cmp_to_int(result):
    return -1 if result else 0 if result is None else 1


def cmp(a, b):
    if type(a) == int and type(b) == list:
        return cmp([a], b)
    if type(a) == list and type(b) == int:
        return cmp(a, [b])
    if type(a) == list and type(b) == list:
        for lhs, rhs in zip(a, b):
            x = cmp(lhs, rhs)
            if x is not None:
                return x
        return cmp(len(a), len(b))
    if a == b:
        return None
    return a < b



with open('input.txt') as f:
    arr = [list(map(eval, x.splitlines())) for x in f.read().split('\n\n')]
    res = sum([cmp(x, y) * (i + 1) for i, (x, y) in enumerate(arr)]) # first part solution
    print(res)

    c = []
    for x in arr:
        c.append(x[0])
        c.append(x[1])

    c += [[[2]], [[6]]]

    sorted_arr = sorted(c, key=functools.cmp_to_key(lambda lhs, rhs: cmp_to_int(cmp(lhs, rhs))))
    res2 = prod([i + 1 for i, x in enumerate(sorted_arr) if x == [[2]] or x == [[6]]]) # second part solution
    print(res2)
