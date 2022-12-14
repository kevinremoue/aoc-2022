import itertools as it

# input = open('day13/test.txt', 'r').read().split("\n\n")
input = open('day13/input.txt', 'r').read().split("\n\n")

def is_right_order(left, right):

    #if one of the list runs out 
    if left is None:
        return -1
    if right is None:
        return 1

    #if int and int
    if isinstance(left, int) and isinstance(right, int):
        print("Comparing INT: ", left, " and ", right)
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    #List and list
    elif isinstance(left, list) and isinstance(right, list):
        print("Comparing LIST: ", left, " and ", right)
        for l, r in it.zip_longest(left, right):
            if (result := is_right_order(l, r)) != 0:
                return result
        return 0
    #if list and int
    else:
        if isinstance(left, int):
            return is_right_order([left], right)
        else:
            return is_right_order(left, [right])

left = []
right = []
for line in input:
    tempo1,tempo2 = line.split("\n")
    left.append(eval(tempo1))
    right.append(eval(tempo2))

indices = 0
result = []
for i in range(len(left)):
    print("=== Pair", i+1, "===")
    if is_right_order(left[i], right[i]) == -1:
        print("=== Pair", i+1, " is OK ===")
        indices = i+1
        result.append(indices)
    else: 
        print("=== Pair", i+1, " is NOT OK ===")

# print(result)
print(sum(result))
