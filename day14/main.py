import numpy as np

#Try with dict

#Build rock paths, array of array of coordinates
def build_rock_paths(input):
    paths = []
    global NB_ROW 
    global NB_COL 

    for line in input:
        coords = line.split("->")
        path = []
        for elt in coords:
            coord = elt.rstrip().split(",")
            col = int(coord[0])
            row = int(coord[1])
            if col > NB_COL:
                NB_COL = col+1
            if row > NB_ROW:
                NB_ROW = row+1
            path.append([col,row])
        paths.append(path)
    return paths

def add_path_in_matrix(path, matrix):
    print(path)
    for idx_part in range(0, len(path)-1, 1):
        print("Processing part", path[idx_part], "and", path[idx_part+1])
        x = path[idx_part][0]
        y = path[idx_part][1]

        #if x going postively
        if path[idx_part][0] - path[idx_part+1][0] < 0:
            while x <= path[idx_part+1][0]:
                print("Adding rock in", x,y)
                matrix[x,y] = 1
                x+=1
        #else negatively
        elif path[idx_part][0] - path[idx_part+1][0] > 0:
            while x >= path[idx_part+1][0]:
                print("Adding rock in", x,y)
                matrix[x,y] = 1
                x-=1
        #y position is moving
        else:
            #if y going positively
            if path[idx_part][1] - path[idx_part+1][1] < 0:
                while y <= path[idx_part+1][1]:
                    print("Adding rock in", x,y)
                    matrix[x,y] = 1
                    y+=1
            #else negatively
            elif path[idx_part][1] - path[idx_part+1][1] > 0:
                while y >= path[idx_part+1][1]:
                    print("Adding rock in", x,y)
                    matrix[x,y] = 1
                    y-=1
    return matrix

def build_matrix(input):
    global NB_ROW 
    global NB_COL 
    #Build rock path
    paths = build_rock_paths(input)
    print("MAX X",NB_COL,"MAX Y",NB_ROW)
    #Build matrix
    matrix = np.zeros((NB_COL,NB_ROW), dtype=int)

    #Build rock path inside matrix
    for path in paths:
        matrix = add_path_in_matrix(path, matrix)

    return matrix

def pour_sand(matrix):
    global START_SAND
    sandx = START_SAND[0]
    sandy = START_SAND[1]

    while sandx <= NB_COL and sandy <= NB_ROW:
        

    #is going out of bound so we stop
    return matrix, False

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

# input = open('day14/input.txt', 'r').read().rstrip().split("\n")
input = open('day14/test.txt', 'r').read().rstrip().split("\n")

NB_ROW = 0
NB_COL = 0
START_SAND = [500,0]
count = 0
#Create matrix detecting max values and adding rock paths
matrix = build_matrix(input)

isTrue = True

print(matrix)

#Pour the sand until it is finished
while isTrue :
    matrix,isTrue = pour_sand(matrix)
    count+=1

print(count)