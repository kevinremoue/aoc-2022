
def find_letter(string):
    firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
    common = ''.join(set(firstpart).intersection(secondpart))
    return(common)

def compute_points(letter):
    if letter.islower():
        return ord(letter)-96
    else:
        return ord(letter)-38

def find_prio(string1, string2, string3):
    strings=[]
    strings.append(string1)
    strings.append(string2)
    strings.append(string3)
    prio = set.intersection(*map(set,strings))
    return str(list(prio)[0])

# input = open('day4/input.txt', 'r')
input = open('day4/test.txt', 'r')

measures = input.read().split("\n")

part1 = []
part2 = []

for string in measures:
    letter=find_letter(string)
    part1.append(compute_points(letter))

print("part1: " +  str(sum(part1)))

for i in range(0,len(measures) - 2, 3):
    prio=find_prio(measures[i], measures[i+1],measures[i+2])
    part2.append(compute_points(prio))

print("part2: " +  str(sum(part2)))
