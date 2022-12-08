import numpy as np

def build_matrix(input):
    global NB_ROW 
    NB_ROW = sum(1 for line in input)
    global NB_COL 
    NB_COL = len(input[0])
    matrix = np.zeros((NB_ROW, NB_COL)).astype(int)

    i = 0 
    for line in input:
        j = 0 
        for character in line:
            matrix[i,j] = int(character)
            j += 1
        i += 1
    return matrix

def is_tree_visible(row, col, tree):
    left = True 
    right = True
    top = True
    bottom = True

    #from left
    for j in range(0,col):
        if matrix[row,j] >= tree:
            left = False

    #from right
    for j in range(NB_COL-1,j+1, -1):
        if matrix[row,j] >= tree:
            right = False

    #from top
    for i in range(0,row):
        if matrix[i,col] >= tree:
            top = False

    #from bottom
    for i in range(NB_ROW-1,row, -1):
        if matrix[i,col] >= tree:
            bottom = False

    return left or right or top or bottom

def get_interior_trees(matrix):
    result = 0
    #We ignore trees on the edge
    for i in range(1,NB_ROW-1):
        for j in range(1,NB_COL-1):
            if is_tree_visible(i,j, matrix[i,j]):
                result+=1
    return result

def get_distance(row, col, tree):
    left = 0
    right = 0
    top = 0
    bottom = 0

    #left
    for j in range(col-1,0-1,-1):
        left+=1
        if tree <= matrix[row,j]:
            break

    #right
    for j in range(col+1,NB_COL, 1):
        right +=1
        if tree <= matrix[row,j]:
            break

    #top
    for i in range(row-1,0-1,-1):
        top +=1
        if tree <= matrix[i,col]:
            break

    #bottom
    for i in range(row+1,NB_ROW, 1):
        bottom +=1
        if tree <= matrix[i,col]:
            break

    # print("value ", tree, row, col, "| total ",  (left * right * top * bottom), "| left ", left, " right ", right, "top ", top, "bottom ", bottom) 
    return (left * right * top * bottom)

def part1(matrix):

    #Edges
    result = 0
    edges = NB_ROW * 2 + NB_COL * 2 - 4
    print("edges: ", edges)
    result = edges

    #interior
    interior = get_interior_trees(matrix)
    print("interior: ", interior)
    result += interior

    print("part1: ", result)

def part2(matrix):
    distance = 0

    for row in range(0,NB_ROW):
        for col in range(0,NB_COL):
            new_distance = get_distance(row,col, matrix[row,col])
            if new_distance > distance:
                distance = new_distance

    print("part2:", distance)



input = open('day8/input.txt', 'r').read().split("\n")
# input = open('day8/test.txt', 'r').read().split("\n")
matrix = build_matrix(input)
print(NB_ROW, NB_COL)
part1(matrix)
part2(matrix)
