class Grain:
    def __init__(self, squares: int):
        if not (1 <= squares <= 64):
            raise ValueError("Squares must be between 1 and 64")
        self.squares = squares

    def calc(self):
        total = 1
        combined_total = 1
        self.mylist = [0]
        for i in range(1, self.squares + 1):
            self.mylist.append(total)
            total = total * 2
        self.combined_total = sum(self.mylist)
        return self.combined_total

if __name__ == "__main__":
    fields = int(input("How many squared so you wish to populate with grains?: "))
    var = Grain(fields)
    var.calc()
    print(f"total amount of grains: {var.combined_total}")
    print(f"total amount of squares: {var.squares}")
    squareposition = int(input("What square do you want to check for grains?: "))
    if (64 >=squareposition >= 1):
        try:
            print(f"total amounts of grains on square {var.mylist[squareposition]}")
        except:
            raise ValueError(f"the value you entered must be between 1 and {fields}")
    else:
        raise ValueError(f"the value you entered must be between 1 and {fields}")
