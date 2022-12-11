import math 

class Monkey():

    items = []
    operation = [] # operator, value 
    division = [] # nb, true, false
    nb_total_inspection = 0

    def __init__(self, items, operation, division):
        self.items = items
        self.operation = operation
        self.division = division

    def test_item(self, item):
        #count as inspection
        self.nb_total_inspection += 1

        #Detect value
        value = 0
        if self.operation[1] == "old":
            value = item
        else:
            value = int(self.operation[1])
        #Detect operator and calculate
        match self.operation[0]:
            case "+":
                item = item + value
            case "-":
                item = item - value
            case "*":
                item = item * value
            case other:
                print("Worry level calculation failed")
        #Apply Bored level
        #no more //3, we must keep small numbers
        gcd = math.gcd(*self.items)
        item = item // gcd
        return item

    def throw_item(self, item, index):
        number = self.division[0]
        if item % number == 0:
            return self.division[1]
        else:
            return self.division[2]

    def get_item(self, item):
        self.items.append(item)

    def clean_items(self):
        self.items = []

    def __str__(self):
        string = self.items
        return str(string)

def get_business(monkeys):
    total = []
    for index, monkey in enumerate(monkeys):
        print("Monkey: ", index, " inspected ", monkey.nb_total_inspection)
        total.append(monkey.nb_total_inspection)
    total.sort()

    print("Monkey Business level: ", total[-1]*total[-2])


#Init values
rounds = 10000
#array of monkeys for test input
monkeys = []
monkey0 = Monkey([79, 98], ["*", "19"], [23,2,3])
monkeys.append(monkey0)

monkey1 = Monkey([54, 65, 75, 74], ["+", "6"], [19,2,0])
monkeys.append(monkey1)

monkey2 = Monkey([79, 60, 97], ["*", "old"], [13,1,3])
monkeys.append(monkey2)

monkey3 = Monkey([74], ["+", "3"], [17,0,1])
monkeys.append(monkey3)

#array of monkeys
# monkeys = []

# monkey0 = Monkey([89, 84, 88, 78, 70], ["*", "5"], [7,6,7])
# monkeys.append(monkey0)

# monkey1 = Monkey([76, 62, 61, 54, 69, 60, 85], ["+", "1"], [17,0,6])
# monkeys.append(monkey1)

# monkey2 = Monkey([83, 89, 53], ["+", "8"], [11,5,3])
# monkeys.append(monkey2)

# monkey3 = Monkey([95, 94, 85, 57], ["+", "4"], [13,0,1])
# monkeys.append(monkey3)

# monkey4 = Monkey([82, 98], ["+", "7"], [19,5,2])
# monkeys.append(monkey4)

# monkey5 = Monkey([69], ["+", "2"], [2,1,3])
# monkeys.append(monkey5)

# monkey6 = Monkey([82, 70, 58, 87, 59, 99, 92, 65], ["*", "11"], [5,7,4])
# monkeys.append(monkey6)

# monkey7 = Monkey([91, 53, 96, 98, 68, 82], ["*", "old"], [3,4,2])
# monkeys.append(monkey7)

for i in range(rounds):
    #each rounds
    print(i)
    for monkey in monkeys:
        #each turns in a round
        #take first item
        for index, item in enumerate(monkey.items):
            #multiply with operation
            item = monkey.test_item(item)
            #test for division and get monkey number 
            nb_monkey = monkey.throw_item(item, index)
            #throw to the right monkey
            monkeys[nb_monkey].get_item(item)
        #redo for the next item
        #Clean monkeys items that have been thrown already
        monkey.clean_items()
    #redo for next monkey

for monkey in monkeys:
    print(monkey)

get_business(monkeys)