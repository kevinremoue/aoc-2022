

def build_section(elf):
    current_array = elf.split("-")
    desired_array = [int(numeric_string) for numeric_string in current_array]
    return desired_array

def test_overlap(sec1, sec2):
    if (sec1[0] >= sec2[0]) & (sec1[1] <= sec2[1]):    
        return True
    elif (sec2[0] >= sec1[0]) & (sec2[1] <= sec1[1]):     
        return True
    else:
        return False

def test_overlap_2(sec1, sec2):
    set1 = set()
    set2 = set()
    for x in range(sec1[0], sec1[1]+1, 1):
        set1.add(x)
    for x in range(sec2[0], sec2[1]+1, 1):
        set2.add(x)

    print(set1)
    print(set2)
    if set1.intersection(set2):
        return True
    else:
        print(False)
        return False


input = open('day4/input.txt', 'r')
# input = open('day4/test.txt', 'r')

measures = input.read().split("\n")

part1 = 0
part2 = 0

for section in measures:
    elf1, elf2 =section.split(",")
    s_1 = build_section(elf1)
    s_2 = build_section(elf2)
    if test_overlap(s_1,s_2):
        part1 += 1

    if test_overlap_2(s_1,s_2):
        part2 += 1
#     part1.append(compute_points(letter))

print(part1)
print(part2)
# for i in range(0,len(measures) - 2, 3):
#     prio=find_prio(measures[i], measures[i+1],measures[i+2])
#     part2.append(compute_points(prio))


# print("part1: " +  str(sum(part1)))
# print("part2: " +  str(sum(part2)))
