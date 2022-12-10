with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


class CPU:
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.signal_strength = 0
        self.part_one = False
        self.screen = ""

    def execute_cycle(self):
        self.cycle += 1
        if self.part_one and self.cycle % 40 == 20:
            self.signal_strength += self.cycle * self.X
        elif self.part_one is False:
            if self.X - 1 <= (self.cycle - 1) % 40 <= self.X + 1:
                self.screen += '#'
            else:
                self.screen += '.'

    def nop(self):
        self.execute_cycle()

    def addx(self, x):
        self.execute_cycle()
        self.execute_cycle()
        self.X += x

    def run(self, lines):
        for ln in lines:
            if ln.split()[0] == 'noop':
                self.nop()
            else:
                self.addx(int(ln.split()[1]))
        if self.part_one:
            print(self.signal_strength)
        else:
            for x in range(len(self.screen)):
                if x % 40 == 0:
                    print(self.screen[x])
                else:
                    print(self.screen[x], end='')

cpu = CPU()
cpu.run(lines)
