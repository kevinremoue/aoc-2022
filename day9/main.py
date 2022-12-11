class Pair:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.tail_positions = {tuple([0, 0])}

    def get_direction(self, direction):
        if direction == "L":
            self.move(position=[self.head[0]-1, self.head[1]])
        elif direction == "R":
            self.move(position=[self.head[0]+1, self.head[1]])
        elif direction == "U":
            self.move(position=[self.head[0], self.head[1]+1])
        elif direction == "D":
            self.move(position=[self.head[0], self.head[1]-1])

    def move(self, position):
        self.head = position
        diff = [0,0]
        for i in range(2):
            diff[i] = self.head[i] - self.tail[i]
        #No need to do anything
        if abs(diff[0]) <= 1 and abs(diff[1]) <=1:
            return 
        #Diag
        elif abs(diff[0]) == 2 and abs(diff[1]) == 2:
            self.tail[0] += diff[0] / 2
            self.tail[1] += diff[1] / 2
        #X diff
        elif abs(diff[0]) == 2:
            self.tail[0] += diff[0] / 2
            self.tail[1] = self.head[1]
        #Y diff
        elif abs(diff[1]) == 2:
            self.tail[0] = self.head[0]
            self.tail[1] += diff[1] / 2
        self.tail_positions.add(tuple(self.tail))
        
input = open('day9/input.txt', 'r').read().split("\n")
# input = open('day9/test2.txt', 'r').read().split("\n")

pair = Pair()
for row in input:
    direction, count = row.rstrip().split(' ')
    for x in range(int(count)):
        pair.get_direction(direction)

print("part1: ", len(pair.tail_positions))

rope = [Pair() for x in range(9)]
for row in input:
    direction, count = row.rstrip().split(' ')
    for x in range(int(count)):
        #calculate head
        rope[0].get_direction(direction)
        #move the rest
        for y in range(8):
            rope[y+1].move(rope[y].tail)

print("part2: ", len(rope[8].tail_positions))