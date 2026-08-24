import os
from pathlib import Path

filename = f"{Path.home()}/.config/todopy/todo.txt"
dirname = f"{Path.home()}/.config/todopy/"

if os.path.exists(filename):
    pass
else:
    with open(filename, "w") as f:
        f.write("General TO-DO list!\n")

if os.path.exists(dirname):
    pass
else:
    os.mkdir(dirname)


class Prompt:
    def __init__(self):
        pass

    def welcome(self):
        print(f"1. List todo files")
        print(f"2. Append to todo files")
        print(f"3. Remove Lines from todo files")
        print(f"4. Delete todo files")
        self.number_of_options = 4
        return self.number_of_options

    def process_input(self):
        while True:
            match main_input:
                case 1:
                    todo.read_dir()
                    break
                case 2:
                    todo.get_file_path()
                    n = 1
                    for i in todo.names_of_filepaths:
                        print(f"{n}. {i}")
                        n += 1
                    print("")
                    sub_input = int(input("Which file do you wish to append to?:\n"))
                    print("")
                    todo_file = todo.list_of_filepaths[sub_input - 1]
                    todo.append_file(todo_file)
                    break
                case 3:
                    todo.read_dir()
                    break
                case 4:
                    todo.read_dir()
                    break


class Todo:
    def __init__(self):
        pass

    def read_file(self, todo_file: str):
        with open(todo_file, "r") as f:
            self.read = f.read()
        return self.read

    def get_file_path(self):
        self.list_of_filepaths = list()
        self.names_of_filepaths = list()
        for e in os.scandir(dirname):
            if e.is_file():
                self.list_of_filepaths.append(e.path)
                self.names_of_filepaths.append(e.name)
        return self.list_of_filepaths, self.names_of_filepaths

    def read_dir(self):
        for e in os.scandir(dirname):
            if e.is_file():
                with open(e.path, "r") as f:
                    print(f"{e.name}:")
                    print(f"{f.readline().rstrip('\n')}")
                    print("")

    def append_file(self, todo_file: str):
        with open(todo_file, "a") as f:
            self.append = f.write(
                input(f"What do you wish to append to your TO-DO entry?:\n") + "\n"
            )
        return self.append


if __name__ == "__main__":
    todo = Todo()
    welcome = Prompt()
    welcome.welcome()
    try:
        main_input = int(input(f"\nSelect an option:\n"))
        print("")
    except ValueError:
        print("Input must be an integer!")
    if main_input not in [i for i in range(1, welcome.number_of_options + 1)]:
        raise Exception(f"Input must range from 1 to {welcome.number_of_options}")
    welcome.process_input()
