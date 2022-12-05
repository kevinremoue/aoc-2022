import numpy as np

def get_index_last_item_from_row(row):
    index = 0
    count = len(row)-1
    for i in reversed(range(len(row)-1)):
        if row[i] != 0:
            break
        count -=1
    return count


def execute_move(move, matrix):
    format = move.split(" ")
    nb_move = int(format[1])
    from_row = int(format[3])-1
    to_row = int(format[5])-1
    for move in range(nb_move):
        #get top crate:
        from_last_item_index = get_index_last_item_from_row(matrix[from_row])
        to_last_item_index = get_index_last_item_from_row(matrix[to_row])
        #move crate:
        print("Move crate from row " + str(from_row) + str(from_last_item_index) + " to " + str(to_row) + str(to_last_item_index))
        
        value = matrix[from_row][from_last_item_index]
        value2 = matrix[to_row][to_last_item_index]

        matrix[to_row][to_last_item_index] = value
        matrix[from_row][from_last_item_index] = value2

        print(matrix)
    return matrix

# input = open('day5/input.txt', 'r')
input = open('day5/test.txt', 'r')

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


for move in moves:
    matrix = execute_move(move, matrix)


part1 = 0
part2 = 0

print("-----results-----")
print(part1)
print(part2)
