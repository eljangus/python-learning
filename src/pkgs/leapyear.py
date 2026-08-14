class Year:
    def __init__(self, year):
        self.year = year

    def isleapyear(self):
        if self.year % 100 == 0:
            if self.year % 400 == 0:
                print("it's a leap year!")
            else:
                print("it's not a leap year!")
        elif self.year % 4 == 0:
            print("it's a leap year!")
        else:
            print("it's not a leap year!")


y1 = Year(int(input("input your year: ")))
y1.isleapyear()
