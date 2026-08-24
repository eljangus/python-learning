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
                    print(f"Header of {e.name}:")
                    print(f"{f.readline().rstrip("\n")}\n")

    def append_file(self, todo_file):
        with open(todo_file, "a") as f:
            self.append = f.append(
                input(f"What do you wish to append to your TO-DO entry?:\n")
            )
        return self.append
