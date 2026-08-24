import os
from pathlib import Path

filename = f"{Path.home()}/.config/todopy/todo.txt"
dirname = f"{Path.home()}/.config/todopy/"

if os.path.exists(filename):
    pass
else:
    os.mkdir(dirname)
    with open(filename, "w") as f:
        pass


class Todo:
    def __init__(self):
        pass

    def read_file(self, todo_file):
        with open(todo_file, "r") as f:
            self.read = f.read()
        return self.read

    def read_dir(self):
        for e in os.scandir(dirname):
            if e.is_file():
                with open(e.path, "r") as f:
                    print(f"\nHeader of {e.name}:")
                    print(f"{f.readline().rstrip("\n")}")

    def append_file(self, todo_file):
        with open(todo_file, "a") as f:
            self.append = f.append(
                input(f"What do you wish to append to your TO-DO entry?:\n")
            )
        return self.append


obj = Todo()
while True:
    print(f"1. List todo files")
    print(f"2. Append to todo files")
    print(f"3. Remove Lines from todo files")
    try:
        input = int(input(f"\nSelect an option:\n"))
    except ValueError:
        print("Input must be an integer!")
    if input not in [1, 2, 3]:
        raise Exception("Input must range from 1 to 3")
    match input:
        case 1:
            obj.read_dir()
            break
        case 2:
            obj.read_dir()
            break
        case 3:
            obj.read_dir()
            break
