import os
from pathlib import Path

dirname = f"{Path.home()}/.config/todopy/"
file_list = list()


class Prompt:
    def __init__(self):
        pass

    def welcome(self):
        print(f"1. List todo lists")
        print(f"2. Append to todo lists")
        print(f"3. Remove Lines from todo lists")
        print(f"4. Delete todo lists")
        self.number_of_options = 4
        return self.number_of_options

    def recursively_print_lists(self):
        n = 1
        for i in todo.names_of_filepaths:
            print(f"{n}. {i}")
            n += 1

    def process_input(self):
        while True:
            match main_input:
                case 1:
                    print("Following todo lists exist:\n")
                    todo.read_dir()
                    break
                case 2:
                    todo.get_file_path()
                    self.recursively_print_lists()
                    print("")
                    sub_input = int(input("Which file do you wish to append to?:\n"))
                    print("")
                    todo_file = todo.list_of_filepaths[sub_input - 1]
                    todo.append_file(todo_file)
                    break
                case 3:
                    todo.get_file_path()
                    break
                case 4:
                    todo.read_dir()
                    break


class Todo:
    def __init__(self):
        pass

    def create_file(self, filename: str):
        with open(f"{dirname}/{filename}.txt", "w") as f:
            header = input(
                "What should be the header of the newly created todo list?:\n"
            )
            f.write(f"{header}\n")

    def read_file(self, todo_file: str):
        with open(todo_file, "r") as f:
            self.file_content = f.read()
        return self.file_content

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
        while True:
            self.read_file(todo_file)
            print(self.file_content)
            with open(todo_file, "a") as f:
                f.write(
                    f"- "
                    + input(f"What do you wish to append to your TO-DO entry?:\n")
                    + "\n"
                )
            check_if_done = input(f"\nWas that all? (y/n):\n")
            print("")
            check_if_done = check_if_done.strip().lower()
            if check_if_done == "y":
                self.read_file(todo_file)
                print(f"\n{self.file_content}")
                break
            elif check_if_done == "n":
                pass
            else:
                raise Exception("Input must be either y or n!")


if os.path.exists(dirname):
    pass
else:
    os.mkdir(dirname)

for e in os.scandir(dirname):
    if e.is_file():
        with open(e.path, "r") as f:
            file_list.append(e.path)

todo = Todo()
if file_list == []:
    is_file_initialised = False
    creation_user_input = input(
        "Welcome to your python TO-DO list!\nIt seems you haven't yet created a todo list, would you wish to do so? (y/n):\n"
    )
    creation_user_input = creation_user_input.lower().strip()
    print("")
    if creation_user_input == "y":
        filename = input("What should be the filename?:\n")
        print("")
        filename = filename.strip().lower()
        todo.create_file(filename)
        is_file_initialised = True
    elif creation_user_input == "n":
        pass
    else:
        raise Exception("You must either enter y or n!")
elif file_list != []:
    is_file_initialised = True
else:
    pass


if __name__ == "__main__":
    welcome = Prompt()
    if is_file_initialised:
        print("\nWelcome to todopy!\n")
        welcome.welcome()
        try:
            main_input = int(input(f"\nSelect an option:\n"))
            print("")
        except ValueError:
            print("Input must be an integer!")
        if main_input not in [i for i in range(1, welcome.number_of_options + 1)]:
            raise Exception(f"Input must range from 1 to {welcome.number_of_options}")
        welcome.process_input()
