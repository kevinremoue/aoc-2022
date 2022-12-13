import numpy as np

def build_matrix(input):
    global NB_ROW 
    NB_ROW = sum(1 for line in input)
    global NB_COL 
    NB_COL = len(input[0])
    print(NB_ROW, NB_COL)
    matrix = np.ndarray([NB_ROW,NB_COL], dtype=int, buffer=None, offset=0, strides=None, order=None)
    i = 0 
    for line in input:
        j = 0 
        for character in line:
            if character == "S":
                start = [i,j]
                matrix[i,j] = ord("a")
            elif character == "E":
                end = [i,j]
                matrix[i,j] = ord("z")
            else:
                matrix[i,j] = ord(character)
            j += 1
        i += 1
    return matrix, start, end

def get_possible_pos(matrix,pos):
    global visited
    positions = []

    #try a neighboor that hasnt been visited
    #check right side
    if pos[1]+1 < NB_COL:
        if (matrix[pos[0],pos[1]+1] - matrix[pos[0],pos[1]] <= 1) or (matrix[pos[0],pos[1]] - matrix[pos[0],pos[1]+1] > 0):
            new_position = [pos[0],pos[1]+1]
            if new_position not in visited:
                positions.append(new_position)
    #check left
    if pos[1]-1 >= 0:
        if matrix[pos[0],pos[1]-1] - matrix[pos[0],pos[1]] <= 1 or (matrix[pos[0],pos[1]] - matrix[pos[0],pos[1]-1] > 0):
            new_position = [pos[0],pos[1]-1]
            if new_position not in visited:
                positions.append(new_position)
    #check up
    if pos[0]-1 >= 0:
        if matrix[pos[0]-1,pos[1]] - matrix[pos[0],pos[1]] <= 1 or (matrix[pos[0],pos[1]] - matrix[pos[0]-1,pos[1]] > 0):
            new_position = [pos[0]-1,pos[1]]
            if new_position not in visited:
                positions.append(new_position)
    #check down
    if pos[0]+1 < NB_ROW:
        if matrix[pos[0]+1,pos[1]] - matrix[pos[0],pos[1]] <= 1 or (matrix[pos[0],pos[1]] - matrix[pos[0]+1,pos[1]] > 0):
            new_position = [pos[0]+1,pos[1]]
            if new_position not in visited:
                positions.append(new_position)

    return positions

def bfs(matrix, start, end):
    global visited
    count = 0
    q1 = []
    q2 = []
    q1.append(start)
    visited.append(start)
    # faire plusieurs queues par niveau de profondeur
    while (end not in q1):
        cell = q1.pop(0)
        positions = get_possible_pos(matrix,cell)
        print(positions)    
        for pos in positions:
            q2.append(pos)
            visited.append(pos)
        if len(q1) == 0:
            count +=1
            #copy
            q1 = q2.copy()
            q2.clear()
    return count

input = open('day12/input.txt', 'r').read().split("\n")
# input = open('day12/test.txt', 'r').read().rstrip().split("\n")

matrix, start, end = build_matrix(input)

visited = []

# print(start)
# print(end)
# print(matrix)

count = bfs(matrix, start, end)
print(count)