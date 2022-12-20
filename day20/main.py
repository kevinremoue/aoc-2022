import copy 

# input = open('day20/input.txt', 'r').read().rstrip().split("\n")
input = open('day20/test.txt', 'r').read().rstrip().split("\n")

encfile = []

for item in input:
    encfile.append(int(item))

index_max = len(encfile)
index = 0
new_file = copy.deepcopy(encfile)


#MIXING:
# print("Init", new_file)


while index<index_max:
    elt = encfile[index]
    current_index = new_file.index(elt)
    new_file.pop(current_index)
    # print("Processing", elt,"at index",current_index )
    if elt+current_index == 0:
        new_file.insert(index_max-1,elt)
    elif elt+current_index < 0:
        new_file.insert(elt+index_max+current_index-1,elt)
    elif elt+current_index > index_max:
        new_file.insert(elt-index_max+current_index+1,elt)
    else:
        new_file.insert(elt+current_index,elt)
    # print("Result", new_file, "\n")
    index+=1
    
#COUNTING:
count = 0
part1 = []
pointer = new_file.index(0)

for count in range(3001):

    if pointer == index_max:
        pointer = 0

    if count == 1000 or count == 2000 or count == 3000:
        part1.append(new_file[pointer])
    pointer +=1
    


print(part1)
print("part1:", sum(part1))