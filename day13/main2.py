import itertools as it
import functools as ft

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

packets = []
for line in input:
    tempo1,tempo2 = line.split("\n")
    packets.append(eval(tempo1))
    packets.append(eval(tempo2))

packets.append([[2]])
packets.append([[6]])

sorted_packets = sorted(packets, key=ft.cmp_to_key(is_right_order))
print((sorted_packets.index([[2]])+1)*(sorted_packets.index([[6]])+1))
