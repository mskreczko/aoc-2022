def find_marker(data, length):
    for i in range(len(data)-length):
        if len(set(data[i:i+length])) == length:
            return i + length

with open('input.txt', 'r') as f:
    data = f.read()
    print(find_marker(data, 4)) # first part solution
    print(find_marker(data, 14)) # second part solution
