input = open('day13/test.txt', 'r').read().split("\n\n")
# input = open('day13/input.txt', 'r').read().split("\n\n")

def is_right_order(list_left, list_right, index_left=0, index_right=0):

    #todo: test 0 then go for list[1:]

    # if len(list_left) == 0 or len(list_right) == 0:
    #     left = list_left[index_left]
    #     right = list_right[index_right]

    #if int and int
    if isinstance(list_left[index_left], int) and isinstance(list_right[index_right], int):
        print("Comparing INT: ", left, " and ", right)
        if left > right:
            return False
        elif left < right:
            return True
        else:
            #Need to go to the next list
            return is_right_order(list_left, list_right, index_left+1, index_right+1)

    #List and list
    elif isinstance(left, list) and isinstance(right, list):
        print("Comparing LIST: ", left, " and ", right)
        for i in range(len(left)):
            #if left longer than right
            if i > len(right)-1:
                print("left longer than right, return false")
                return False
            else:
                print("Going deeper")
                return is_right_order(left,right, i, i)
    #if list and int
    elif isinstance(left, list) and isinstance(right, int):
        print("left is list", left , "right is int", right)
        for i in range(len(left)):
            return is_right_order(left, list_right, i, index_right)
    #if int and list
    elif isinstance(left, int) and isinstance(right, list):
        print("left is int", left , "right is list", right)
        for i in range(len(right)):
            return is_right_order(list_left, right, index_left, i)
                    
left = []
right = []
for line in input:
    tempo1,tempo2 = line.split("\n")
    left.append(eval(tempo1))
    right.append(eval(tempo2))

print(left)
print(right)

indices = 0
result = []
for i in range(len(left)):
    print("=== Pair", i+1, "===")
    if is_right_order(left, right):
        print("=== Pair", i+1, " is OK ===")
        indices = i+1
        result.append(indices)
    else: 
        print("=== Pair", i+1, " is NOT OK ===")

print(result)

