def score(a, b):
    result = 0

    if b == "X":
        result += 1
    elif b == "Y":
        result += 2
    else:
        result += 3
    
    if a == "A" and b == "X":
        result += 3
    elif a == "B" and b == "Y":
        result += 3
    elif a == "C" and b == "Z":      
        result += 3
    elif a == "A" and b == "Y":
        result += 6
    elif a == "B" and b == "Z":
        result += 6
    elif a == "C" and b == "Y":
        result += 0
    elif a == "C" and b == "X":
        result += 6
    elif a == "A" and b == "Z":
        result += 0
    elif a == "B" and b == "X":
        result += 0  
    return result

def cal_play(a, b):
    #lose
    if b == "X":
        if a == "A":
            return "Z"
        elif a == "B":
            return "X"
        elif a == "C":
            return "Y"
    #draw
    elif b == "Y":
        if a == "A":
            return "X"
        elif a == "B":
            return "Y"
        elif a == "C":
            return "Z"
    #Win
    else:
        if a == "A":
            return "Y"
        elif a == "B":
            return "Z"
        elif a == "C":
            return "X"

input = open('day2/input.txt', 'r')
# input = open('day2/test.txt', 'r')

measures = input.read().split("\n")

result = []

print(measures)

for elt in measures:
    strategy = elt.split(" ")
    play=cal_play(strategy[0], strategy[1])
    result.append(score(strategy[0], play))

# print(result)
print(sum(result))