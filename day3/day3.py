def parse(wire_string):
    parsed_wire = []
    for x in wire_string:
        head = x.rstrip('0123456789\n')
        tail = x[len(head):].rstrip('\n')
        parsed_wire += (head, tail)
    return parsed_wire

class WireMap():
    def __init__(self, wire1, wire2):
        self.w1 = wire1
        self.w2 = wire2
        self.max_pos = [-1, 1, -1, 1]
        self.map = []

        self.calc_max_pos() # = [-x, x, -y, y]
        self.calc_size() # = [max x, max y], also gets origin
        self.make_map()

    def calc_max_pos(self):
        wire = self.w1
        for i in range(2):
            pos = [0, 0]
            for idx in range(0, len(wire), 2):
                inst = wire[idx]
                dist = int(wire[idx + 1])

                if inst == "R":
                    pos[0] += dist
                    if pos[0] + 1 > self.max_pos[1]:
                        self.max_pos[1] = pos[0] + 1
                elif inst == "L":
                    pos[0] -= dist
                    if pos[0] - 1 < self.max_pos[0]:
                        self.max_pos[0] = pos[0] - 1
                elif inst == "U":
                    pos[1] += dist
                    if pos[1] + 1 > self.max_pos[3]:
                        self.max_pos[3] = pos[1] + 1
                elif inst == "D":
                    pos[1] -= dist
                    if pos[1] - 1 < self.max_pos[2]:
                        self.max_pos[2] = pos[1] - 1
                else:
                    print("oh no the spooky has happened")
            wire = self.w2

    def calc_size(self):
        self.cols = self.max_pos[1] - self.max_pos[0] + 1
        self.rows = self.max_pos[3] - self.max_pos[2] + 1
        self.xo = -self.max_pos[0]
        self.yo = self.rows + self.max_pos[2] - 1

    def make_map(self):
        self.map = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.map[self.yo][self.xo] = 'X'

    def draw_map(self):
        wire = self.w1
        for i in range(1, 3):
            pos = [self.yo, self.xo] #(y, x)
            for idx in range(0, len(wire), 2):
                inst = wire[idx]
                dist = int(wire[idx + 1])

                if inst == "R":
                    for x in range(dist):
                        pos[1] += 1
                        self.map[pos[0]][pos[1]] += i
                elif inst == "L":
                    for x in range(1, dist + 1):
                        pos[1] -= 1
                        self.map[pos[0]][pos[1]] += i

                elif inst == "U":
                    for x in range(1, dist + 1):
                        pos[0] -= 1
                        self.map[pos[0]][pos[1]] += i

                elif inst == "D":
                    for x in range(1, dist + 1):
                        pos[0] += 1
                        self.map[pos[0]][pos[1]] += i
                else:
                    print("oh no the spooky has happened")
            wire = self.w2

    def print_map(self):
        for row in self.map:
            for x in range(len(row)):
                print(row[x], end ="")
            print()



# fo = open("input.txt", "r")
# input = fo.readline()
# input = input.split(",")
# wire1 = parse(input)
# input = fo.readline()
# input = input.split(",")
# wire2 = parse(input)


wire1 = parse("R8,U5,L5,D3".split(","))
wire2 = parse("U7,R6,D4,L4".split(","))

wm = WireMap(wire1, wire2)
wm.draw_map()
wm.print_map()
