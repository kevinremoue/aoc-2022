import numpy as np 

#faire une ligne de 0 a 240 pour representer cycles, CRT est a position cycle et drawn
#puis diviser par 40 pour afficher
#sur chaque cycle checker position CRT, si position CRT (cycle modulo 40) == position sprite (= position register +1 -1)

def execute_addx(register, value, current_cycle):
    current_cycle +=1
    compute_signals(current_cycle, register)
    current_cycle +=1
    compute_signals(current_cycle, register)
    register += value

    return current_cycle, register

def compute_signals(current_cycle, register):
    global part2
    global row

    crt = current_cycle - row * 40
    sprite = [register, register+1, register+2]
    if crt in sprite:
        part2.append("#")
    else:
        part2.append(" ")
    
    if current_cycle % 40 == 0:
        row +=1


def render(part2):
    # print(part2[0:39])
    # print(part2[40:79])
    # print(part2[80:119])
    # print(part2[120:159])
    # print(part2[160:199])
    # print(part2[200:239])

    for i in range(1,len(part2)):
        print(part2[i], end='')
        if i % 40 == 0:
            print("")


input = open('day10/input.txt', 'r').read().split("\n")
# input = open('day10/test.txt', 'r').read().split("\n")

cycles = [40,80,120,160,200,240]
current_cycle = 0
row = 0
register = 1
part2 = ['s']

for command in input:
    args = command.split(" ")
    match args[0]:
        case 'noop':
            current_cycle += 1
            compute_signals(current_cycle, register)
        case 'addx':
            current_cycle, register = execute_addx(register, int(args[1]), current_cycle)
        case other:
            print("Something Wrong")

render(part2)

