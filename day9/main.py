import copy

def process_command(command, head, tail, count):
    args = command.split(" ")
    direction = args[0]
    nb = int(args[1])

    for move in range(nb):
        print("Going ", direction)
        head, tail = move_rope(direction, head, tail, count)
        print(head, tail)
        print("--------")
    
    return head, tail

def move_rope(direction, head, tail, count):
    if direction == "L":
        new_x = head[0]-1
        new_y = head[1]
        head = [new_x,new_y]
        head, tail = manage_tail(head, tail, count)
    elif direction == "R":
        new_x = head[0]+1
        new_y = head[1]
        head = [new_x,new_y]
        head, tail = manage_tail(head, tail, count)
    elif direction == "U":
        new_x = head[0]
        new_y = head[1]+1
        head = [new_x,new_y]
        head, tail = manage_tail(head, tail, count)
    elif direction == "D":
        new_x = head[0]
        new_y = head[1]-1
        head = [new_x,new_y]
        head, tail = manage_tail(head, tail, count)
    return head, tail

def manage_tail(head, tail, count):
    print("incoming tail: ", tail)
    #check space on the left 
    if head[0] - tail[0] == -2:
        tail[0] = head[0]+1
        tail[1] = head[1]
        new_tail = copy.copy(tail)
        if new_tail not in count:
            count.append(new_tail)
    #right
    elif head[0] - tail[0] == 2:
        tail[0] = head[0]-1
        tail[1] = head[1]
        new_tail = copy.copy(tail)
        if new_tail not in count:
            count.append(new_tail)
    #bottom
    elif head[1] - tail[1] == -2:
        tail[0] = head[0]
        tail[1] = head[1]+1
        new_tail = copy.copy(tail)
        if new_tail not in count:
            count.append(new_tail)
    #up
    elif head[1] - tail[1] == 2:
        tail[0] = head[0]
        tail[1] = head[1]-1
        new_tail = copy.copy(tail)
        if new_tail not in count:
            count.append(new_tail)
    print("outcoming tail: ", tail)
    print("count ", count)
    return head, tail

input = open('day9/input.txt', 'r').read().split(" \n")
# input = open('day9/test.txt', 'r').read().split("\n")

#initially at 0,0 (x,y)
tail = [0,0]
head = [0,0]
count = []
#starting position
count.append([0,0])

print(head,tail)

for command in input:
    head, tail = process_command(command, head, tail, count)


print(count)
print("part1: ", len(count))
