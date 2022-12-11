
def execute_addx(register, value, current_cycle):
    current_cycle +=1
    compute_signals(current_cycle, register)
    current_cycle +=1
    compute_signals(current_cycle, register)
    register += value

    return current_cycle, register

def compute_signals(current_cycle, register):
    global signals
    if current_cycle in cycles:
        signal = current_cycle * register
        signals.append(signal)
        print("Cycles: ", current_cycle, "\tregister ",  register, "\tadding ", signal)

input = open('day10/input.txt', 'r').read().split("\n")
# input = open('day10/test.txt', 'r').read().split("\n")

cycles = [20,60,100,140,180,220]
current_cycle = 0
signals = []
register = 1

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

print("part1 ", sum(signals))
