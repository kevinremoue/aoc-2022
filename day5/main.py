import numpy as np

def execute_move_part1(move, dict):
    format = move.split(" ")
    nb_move = int(format[1])
    from_row = int(format[3])
    to_row = int(format[5])
    for move in range(nb_move):
        dict[to_row].append(dict[from_row][-1])
        del dict[from_row][-1]

    return dict


def execute_move_part2(move, dict):
    format = move.split(" ")
    nb_move = int(format[1])
    from_row = int(format[3])
    to_row = int(format[5])
    dict[to_row] += dict[from_row][-nb_move:]
    del dict[from_row][-nb_move:]
    return dict    

input = open('day5/input.txt', 'r')
# input = open('day5/test.txt', 'r')

measures = input.read().split("\n\n")
crates = measures[0].split("\n")
moves = measures[1].split("\n")

nb_column = len(crates[-1].split("  "))
nb_row = len(crates)-1

matrix = np.zeros((nb_row, nb_column))

for i in range(len(crates)-1):
    line_of_crates = crates[i].replace("    ", " ").split(" ")
    for j in range(len(line_of_crates)):
        if line_of_crates[j] != '':
            tempo = list(line_of_crates[j])
            #Using Ascii
            matrix[i][j] = ord(tempo[1])

matrix = np.rot90(matrix, k=1, axes=(1,0))

print(matrix)

#matrix into dict without 0
dict = {}

for i in range(len(crates)):
    new_list = []
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            new_list.append(matrix[i][j])
    dict[i+1] = new_list


for move in moves:
    # dict = execute_move_part1(move, dict)
    dict = execute_move_part2(move, dict)

print(dict)

char_dict = {}
for i in range(len(dict)):
    print(chr(int(dict[i+1][-1])))
