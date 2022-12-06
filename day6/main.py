

def get_char(string, seq):
    markers = []
    count = 0
    for i in range(0,len(string)-seq-1, 1):
        markers = string[i:i+seq]
        if len(markers) == len(set(markers)):
            return count + seq
        count += 1
        
input = open('day6/input.txt', 'r')
# input = open('day6/test.txt', 'r')

string = input.read()
p1 = get_char(string, 4)
p2 = get_char(string, 14)

print(p1)
print(p2)