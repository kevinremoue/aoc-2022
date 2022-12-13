input = open('day13/test.txt', 'r').read().split("\n\n")
# input = open('day13/input.txt', 'r').read().split("\n\n")

def is_right_order(left, right):

    if isinstance(left, list) and isinstance(right, list):
        print("checking: ", left, " and ", right)
        is_right_order(left.pop(0),right.pop(0))
    else:
        if left > right:
            return False
        else: 
            return True
    # #if left run out of item
    # if len(right) - len(left) > 0:
    #     result = True
    # #if right run out of item
    # elif len(left) - len(right) > 0:
    #     result = False


    # for i in range(0, len(left), 1):
    #     result = result & is_right_order(left,right)
        
    # #if left side smaller than right side
    # #return true
    # #else
    # #return false

    # return result



left = []
right = []
for line in input:
    tempo1,tempo2 = line.split("\n")
    left.append(eval(tempo1))
    right.append(eval(tempo2))

print(left)
print(right)

indices = 0

for i in range(len(left)):
    if is_right_order(left, right):
        indices += i+1

print(indices)

