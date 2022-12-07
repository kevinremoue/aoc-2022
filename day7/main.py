class TreeNode:

    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self):
        string = self.name + " size: " + str(self.size) + "\n\t" + str(self.parent)
        return string
        
# input = open('day7/input.txt', 'r')
input = open('day7/test.txt', 'r')
commands = input.read().split("\n")


current_folder = TreeNode("/", 0) 
head = current_folder

command_mode = ""
depth = 0

for command in commands[1:]:
    parsed_cmd = command.split(" ")
    #if it is a command input, get the command
    if parsed_cmd[0] == "$":
        if parsed_cmd[1] == "ls":
            command_mode = "ls"
        elif parsed_cmd[1] == "cd":
            command_mode = "cd"
            if parsed_cmd[2] == "..":
                depth -=1
                current_folder = current_folder.parent
            else:
                depth +=1
                new_dir = TreeNode(parsed_cmd[2], 0, current_folder)
                current_folder = new_dir
    elif command_mode == "ls":
        if command[0] == "dir":
            new_dir = TreeNode(parsed_cmd[1], 0, current_folder)
        else:
            new_file = TreeNode(parsed_cmd[1], parsed_cmd[0], current_folder)

print(head)
