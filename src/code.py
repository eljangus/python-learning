def getnumbers():
    firstnum = float(input("first number: "))
    operator = input("operator: ")
    secondnum = float(input("second num: "))
    return firstnum, operator, secondnum


def check(firstnum, operator, secondnum):
    print(firstnum, operator, secondnum)
    checking = input("is this correct? (y/n): ")
    return checking


def calculate(firstnum, operator, secondnum):
    match operator:
        case "+":
            print(firstnum + secondnum)
        case "-":
            print(firstnum - secondnum)
        case "*":
            print(firstnum * secondnum)
        case "/":
            print(firstnum / secondnum)


def calculator():
    while True:
        firstnum, operator, secondnum = getnumbers()
        checking = check(firstnum, operator, secondnum)

        if checking == ("y"):
            calculate(firstnum, operator, secondnum)
            break
        elif checking == ("n"):
            print("Let's try again.\n")
        else:
            print("go kys retard")
            break

calculator()
