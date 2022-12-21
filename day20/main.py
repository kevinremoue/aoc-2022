import copy 


#2692 too low

input = open('day20/input.txt', 'r').read().rstrip().split("\n")
# input = open('day20/test.txt', 'r').read().rstrip().split("\n")

encfile = []

for item in input:
    encfile.append(int(item))

index_max = len(encfile)
index = 0
new_file = copy.deepcopy(encfile)

def mix_file(encfile):
    new_file = copy.deepcopy(encfile)
    index_max = len(encfile)

    for index, elt in enumerate(encfile):
        new_file_number = new_file[new_file.index(elt)]
        current_index = new_file.index(new_file_number)
        # print("Processing", elt, "at index", current_index )
        if current_index + elt == 0:
            new_index = index_max-1
        elif current_index + elt < 0:
            new_index = ((current_index + elt) % index_max) -1
        elif current_index + elt > index_max:
            new_index = ((current_index + elt) % index_max) +1
        else:
            new_index = current_index + elt % index_max
        # print("Going to index", new_index)
        new_file.pop(current_index)
        new_file.insert(new_index, elt)
        # print("Result", new_file, "\n")
    return new_file


#MIXING:
print("Init", encfile)
new_file = mix_file(encfile)

print(new_file)

    
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