
class Node:
    def __init__(self, name, parent, size, isFolder):
        self.name = name
        self.parent = parent
        self.size = size
        self.isFolder = isFolder
        self.children = []

    def __str__(self):
        string = self.name
        for child in self.children:
            string += "\n - "
            string += str(child)
        return string

def process_each_size(folder):
    if folder.isFolder:
        for child in folder.children:
            folder.size+=process_each_size(child)
    return folder.size

def get_folders(root):
    folders = []
    if root.isFolder:
        folders.append(root)
        for child in root.children:
            folders.extend(get_folders(child))
    return folders

input = open('day7/input.txt', 'r')
# input = open('day7/test.txt', 'r')
commands = input.read().split("\n")


root = Node("/", None, 0, True) 
current_folder = root

for command in commands[1:]:
    parsed_cmd = command.split(" ")
    #if it is a command input, get the command
    if parsed_cmd[0] == "$":
        if parsed_cmd[1] == "cd":
            #cd ..
            if parsed_cmd[2] == "..":
                current_folder = current_folder.parent
            #cd x
            else:
                new_dir = Node(parsed_cmd[2], current_folder, 0, True)
                current_folder.children.append(new_dir)
                current_folder = new_dir
    elif parsed_cmd[0] != "dir":
        file = Node(parsed_cmd[1], None, int(parsed_cmd[0]),False)
        current_folder.children.append(file)

#Root got the full tree now!
#get the size and then folders with the right size
process_each_size(root)
folders = get_folders(root)
size = 0
for folder in folders:
    if folder.size <= 100000:
        size += folder.size
print("part1 ", size)

#PART2
sizes = []
fs_size = 70000000
needed_size = 30000000
free_space = fs_size - int(folders[0].size)
space_to_clear = needed_size - free_space
print("space to clear ", space_to_clear)

for folder in folders:
    if folder.size >= space_to_clear:
        sizes.append(folder.size)

print(sizes)
print("part2 ", min(sizes))

