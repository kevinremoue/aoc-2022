import copy
import time
#Try with dict

#Build rock paths, array of array of coordinates
def build_rock_paths(input):
    paths = []
    global THRESHOLD
    global X_MAX
    for line in input:
        coords = line.split("->")
        path = []
        for elt in coords:
            coord = elt.rstrip().split(",")
            col = int(coord[0])
            if col > X_MAX:
                X_MAX = col
            row = int(coord[1])
            if row > THRESHOLD:
                THRESHOLD = row
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
                matrix[x,y] = "#"
                x+=1
        #else negatively
        elif path[idx_part][0] - path[idx_part+1][0] > 0:
            while x >= path[idx_part+1][0]:
                print("Adding rock in", x,y)
                matrix[x,y] = "#"
                x-=1
        #y position is moving
        else:
            #if y going poitively
            if path[idx_part][1] - path[idx_part+1][1] < 0:
                while y <= path[idx_part+1][1]:
                    print("Adding rock in", x,y)
                    matrix[x,y] = "#"
                    y+=1
            #else negatively
            elif path[idx_part][1] - path[idx_part+1][1] > 0:
                while y >= path[idx_part+1][1]:
                    print("Adding rock in", x,y)
                    matrix[(x,y)] = "#"
                    y-=1
    return matrix

def build_matrix(input):
    global THRESHOLD
    #Build rock path
    paths = build_rock_paths(input)

    #Build matrix
    matrix = dict()
    #Build rock path inside matrix
    for path in paths:
        matrix = add_path_in_matrix(path, matrix)

    #PART2 we add the floor 
    new_path = [[0, THRESHOLD+2],[X_MAX+500,THRESHOLD+2]]
    matrix = add_path_in_matrix(new_path,matrix)

    return matrix

def pour_sand(matrix):
    global START_SAND
    global THRESHOLD
    new_sand = copy.deepcopy(START_SAND)

    while can_move(matrix,new_sand):
        print("Yes can")
        new_sand = move(matrix,new_sand)
        print("Moved in", new_sand)
        # time.sleep(1)

    #Cannot move anymore, we add it
    print("Adding", (new_sand[0],new_sand[1]))
    #Case if we try to add 500,0 multiple times, meaning that the sand cannot move anymore
    if (new_sand[0],new_sand[1]) in matrix:
        return matrix,False
    matrix[(new_sand[0],new_sand[1])] = "o"
    #is going out of bound so we stop
    return matrix, True

def can_move(matrix,sand):
    print("Can", sand, "moves?")
    sandx = sand[0]
    sandy = sand[1]
    if (sandx,sandy+1) in matrix:
        if (sandx-1,sandy+1) in matrix:
            if (sandx+1,sandy+1) in matrix:
                return False
            else:
                return True
        else:
            return True
    else:
        return True

def move(matrix, sand):
    sandx = sand[0]
    sandy = sand[1]
    if (sandx,sandy+1) not in matrix:
        return (sandx, sandy+1)
    elif (sandx-1,sandy+1) not in matrix:
        return (sandx-1,sandy+1)
    elif (sandx+1,sandy+1) not in matrix:
        return (sandx+1,sandy+1)
    else:
        return (sandx,sandy+1)

input = open('day14/input.txt', 'r').read().rstrip().split("\n")
# input = open('day14/test.txt', 'r').read().rstrip().split("\n")

THRESHOLD = 0
X_MAX = 0
START_SAND = (500,0)
count = 0
#Create matrix detecting max values and adding rock paths
matrix = build_matrix(input)
isTrue = True

# print(matrix)
# print("THRESHOLD:", THRESHOLD)

# Pour the sand until it is finished
# When should we take a new sand ? 
# 
while isTrue :
    print("NEW SAND")
    matrix,isTrue = pour_sand(matrix)
    count+=1

#ignore last one as it is used to detect the end
print(count-1)